# cvpoi

Lý thuyết lập trình thi đấu — trang bài học tương tác kèm lời giải bài tập.
Deploy tại [cvpoi.vercel.app](https://cvpoi.vercel.app).

## Công nghệ

HTML tĩnh thuần, **không có hệ build**. Không `package.json`, không
`vercel.json` — Vercel deploy trực tiếp mọi file `.html`/`.css`/`.js`/`.svg`
trong repo mỗi khi có commit lên `main`.

Chạy thử cục bộ (bắt buộc qua server, không mở trực tiếp bằng `file://` vì
các trang nạp `assets/chuan.css` bằng đường dẫn tương đối):

```bash
python -m http.server 8777
```

rồi mở `http://127.0.0.1:8777/`.

## Cấu trúc

- `index.html` — trang chủ, danh sách chuyên đề.
- `sols/index.html` — kho lời giải, danh sách toàn bộ bài tập có hướng dẫn.
- `<chuyên-đề>/index.html` — trang bài học (`array-1d/`, `tree/`, `string/`…).
- `<chuyên-đề>/<mã-bài>/index.html` (hoặc `<chuyên-đề>/sols/<mã-bài>/`) —
  trang lời giải từng bài.
- `assets/` — bộ giao diện dùng chung: `chuan.css` + `chuan.js` (tách nguyên
  văn từ `ChuyenDe/_template/shell.html`, xem `tools/tach-shell.py`),
  `site.css` (thanh điều hướng + chân trang), `favicon.svg`,
  `html2canvas.min.js` (chép sẵn để trang không gọi CDN).
- `tools/` — script Python bảo trì site, mô tả ở dưới.

## Script trong `tools/`

Tất cả chạy từ thư mục gốc repo, có chế độ xem trước (không tham số) và ghi
thật (`--ghi`). Chạy lại nhiều lần không nhân đôi nội dung.

- **`tach-shell.py`** — tách khối `<style>`/`<script>` của
  `ChuyenDe/_template/shell.html` thành `assets/chuan.css` +
  `assets/chuan.js`. Muốn đổi giao diện chuẩn thì sửa `shell.html` rồi chạy
  lại file này, để tài liệu chuyên đề (PDF/HTML) và website không bao giờ
  lệch nhau.
- **`dong-bo.py`** — đồng bộ thanh điều hướng, chân trang và thẻ metadata
  (`<title>`, `description`, `og:*`) cho mọi trang khai trong dict `TRANG`
  ở đầu file. Trang có thanh mục lục cố định bên trái phải được thêm vào tập
  `CO_THANH_BEN` trong cùng file, nếu không thanh điều hướng sẽ chèn sai chỗ.
- **`len-chuan.py`** — công cụ hỗ trợ (không tự chạy được, các script
  chuyển đổi trang import từ đây) đưa một trang bài học thô về bộ giao diện
  chuẩn: ánh xạ bảng biến màu cũ sang biến của `chuan.css`, xoá quy tắc CSS ở
  mức tài liệu, thu hẹp `button{}` trần vào đúng phòng mô phỏng.
- **`sua-nen-sang.py`** — chèn khối CSS (`/*cv-fix-nen-sang*/`) ép các màu
  gõ cứng còn sót của bản nền tối theo bảng màu của chuẩn, để nội dung đọc
  được ở cả nền sáng lẫn nền tối.
- **`dung-thu-vien-noi-bo.py`** — quét mọi trang tìm thẻ `<script>` trỏ tới
  CDN (cdnjs/jsdelivr) rồi đổi sang bản đã tải về `assets/`, tự tính số
  `../` theo độ sâu thư mục.

## Đăng nhập và phân quyền

Lý thuyết mở cho mọi người; lời giải và tài liệu từng lớp phải đăng nhập.
Việc chặn làm **trên máy chủ Vercel** (`middleware.js` chạy trước mọi trang),
nên trang bị khoá không tới được trình duyệt của người chưa có quyền. Vì vậy
repo GitHub phải để **riêng tư** — repo công khai thì đọc thẳng được nội dung.

- `middleware.js` — kiểm tra phiên và luật; tự trả lời `/api/dang-nhap`,
  `/api/dang-xuat`, `/api/toi`; chặn luôn `_auth/`, `tools/`, `README.md`.
- `_auth/taikhoan.js` — tài khoản (mật khẩu chỉ lưu mã băm). Không sửa tay,
  dùng `tools/tai-khoan.py`.
- `_auth/quyen.js` — luật "thư mục nào cho nhóm nào", sửa tay. Trang không
  khớp luật nào thì mở. Nhóm `giaovien` xem được mọi trang.
- `dang-nhap/index.html` — trang đăng nhập.
- `assets/taikhoan.js` — ô tài khoản trên thanh điều hướng và dấu khoá ở
  liên kết chưa được mở (chỉ là chỉ dẫn, không phải lớp chặn).
- Biến môi trường **`CV_SECRET`** trên Vercel (Project → Settings →
  Environment Variables, ít nhất 32 ký tự ngẫu nhiên) dùng để ký phiên đăng
  nhập. Thiếu biến này thì không ai đăng nhập được; đổi giá trị thì mọi
  người phải đăng nhập lại.

Việc thường làm (xong thì `git commit` + `git push`, khoảng một phút sau có
hiệu lực):

```bash
python tools/tai-khoan.py them an.nv --ten "Nguyễn Văn An" --nhom hsg9
python tools/tai-khoan.py nhap lop9.csv     # cả lớp; mật khẩu ghi ra lop9.matkhau.csv
python tools/tai-khoan.py dat-lai an.nv     # học sinh quên mật khẩu
python tools/tai-khoan.py xoa an.nv
python tools/tai-khoan.py ds
python tools/tai-khoan.py quyen             # soát: trang nào mở, trang nào khoá
```

**Thêm thư mục lời giải mới thì phải thêm một dòng vào `_auth/quyen.js`**,
nếu không trang đó mở cho mọi người. Chạy `tai-khoan.py quyen` để soát.

Chạy thử trên máy có cả lớp đăng nhập (thay cho `python -m http.server`):

```bash
node tools/chay-thu.mjs
```

## Thêm một trang mới

Thêm chuyên đề hoặc lời giải phải ghi danh tay ở đúng 3 chỗ, thiếu một chỗ
là trang không hiện hoặc thanh điều hướng bị lệch:

1. **`index.html`** — mảng `TOPICS` (dòng ~152): thêm một phần tử
   `{slug, name, desc, group, ready:true, icon}` nếu là chuyên đề mới.
2. **`sols/index.html`** — mảng `SOLS` (dòng ~122): thêm một phần tử
   `{code, name, href, group}` nếu là trang lời giải.
3. **`tools/dong-bo.py`** — dict `TRANG` (dòng ~29): thêm một mục khai
   `nhom`/`cha`, `nhan`, `tieude`, `mota` cho trang. Nếu trang có thanh mục
   lục cố định bên trái, thêm luôn đường dẫn vào tập `CO_THANH_BEN`.

Sau đó chạy theo thứ tự:

```bash
python tools/dong-bo.py --ghi
python tools/sua-nen-sang.py --ghi
python tools/dung-thu-vien-noi-bo.py --ghi
```
