# -*- coding: utf-8 -*-
"""
dong-bo.py — làm cho mọi trang HTML của site dùng chung một thanh điều hướng,
một chân trang và một bộ thẻ metadata.

Cách dùng (chạy từ thư mục gốc của repo):

    python tools/dong-bo.py            # xem trước, KHÔNG ghi file
    python tools/dong-bo.py --ghi      # ghi thật

Công cụ chạy lại được nhiều lần mà không nhân đôi: mỗi khối do nó sinh ra đều
được bọc trong cặp chú thích <!--cv-...--> và sẽ bị gỡ trước khi chèn bản mới.

Thêm trang mới thì khai thêm một dòng trong TRANG bên dưới rồi chạy lại.
"""

import os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================================================
#  KHAI BÁO TỪNG TRANG
#    nhom   : tên nhóm hiển thị đầu đường dẫn vụn (khi trang không có cha)
#    cha    : (nhãn, đường dẫn tương đối) của chuyên đề chứa trang này
#    nhan   : tên ngắn của trang, hiện ở cuối đường dẫn vụn
#    tieude : nội dung thẻ <title>, đã bỏ phần " | Lý thuyết CP"
#    mota   : một câu cho thẻ meta description
# =====================================================================
TRANG = {
 'index.html': dict(
    nhom=None, cha=None, nhan=None, tieude='Lý thuyết CP',
    mota='Tuyển tập chuyên đề lập trình thi đấu: lý thuyết, mô phỏng từng bước và bài luyện có lời giải.'),

 # ---------- Chuyên đề ----------
 'io/index.html': dict(
    nhom='Cơ bản', nhan='Nhập xuất dữ liệu', tieude='Nhập xuất dữ liệu trong C++',
    mota='Luật in số thực của cout, fixed và setprecision, chia nguyên và lấy dư, ký tự thoát.'),
 'array-1d/index.html': dict(
    nhom='Cơ bản', nhan='Mảng 1 chiều', tieude='Mảng 1 chiều',
    mota='Duyệt mảng, tìm kiếm tuyến tính, kỹ thuật lính canh và hai con trỏ.'),
 'array-2d/index.html': dict(
    nhom='Cơ bản', nhan='Mảng 2 chiều', tieude='Mảng 2 chiều',
    mota='Lưới hàng nhân cột, cờ hiệu, lính canh hai giá trị lớn nhất.'),
 'string/index.html': dict(
    nhom='Cơ bản', nhan='Xâu ký tự', tieude='Xử lý xâu ký tự trong C++',
    mota='Kiểu char và string, đọc và tách dữ liệu, quét cụm số, xâu con và dãy con, số lớn dạng xâu.'),
 'dsu/index.html': dict(
    nhom='Cấu trúc dữ liệu', nhan='Các tập rời rạc (DSU)', tieude='Các tập rời rạc (DSU)',
    mota='Hợp nhất hai tập, tìm gốc, nén đường đi và hợp theo hạng.'),
 'sqrt-decomposition/index.html': dict(
    nhom='Cấu trúc dữ liệu', nhan='Chia căn', tieude='Chia căn (Sqrt Decomposition)',
    mota='Chia mảng thành khối cỡ căn N để truy vấn và cập nhật cùng nhanh.'),
 'tree/index.html': dict(
    nhom='Đồ thị & cây', nhan='Cây & LCA', tieude='Cây & LCA — nâng nhị phân',
    mota='Duyệt cây bằng DFS và tìm tổ tiên chung gần nhất bằng nâng nhị phân.'),
 'tree/euler-tour/index.html': dict(
    cha=('Cây & LCA', '../index.html'), nhan='Euler Tour', tieude='Euler Tour trên cây',
    mota='Đưa cây về mảng để dùng được các truy vấn đoạn.'),
 'euler-circuit/index.html': dict(
    nhom='Đồ thị & cây', nhan='Chu trình Euler', tieude='Chu trình Euler',
    mota='Điều kiện tồn tại chu trình Euler và thuật toán Hierholzer.'),
 'dp/index.html': dict(
    nhom='Quy hoạch động', nhan='Quy hoạch động', tieude='Quy hoạch động',
    mota='Quy hoạch động trên đoạn, kèm bài luyện có hướng dẫn giải.'),
 'prefix-sum/index.html': dict(
    nhom='Kỹ thuật', nhan='Tổng tiền tố', tieude='Tổng tiền tố',
    mota='Cộng dồn một chiều và hai chiều, mảng hiệu, kết hợp bảng băm.'),
 'prefix-sum/1d/index.html': dict(
    cha=('Tổng tiền tố', '../index.html'), nhan='Tổng tiền tố 1D', tieude='Tổng tiền tố 1D',
    mota='Bài học có mô phỏng từng bước cách dựng mảng cộng dồn và mảng hiệu.'),
 'prefix-sum/prefix-sum-1d/index.html': dict(
    cha=('Tổng tiền tố', '../index.html'), nhan='Chuyên đề tổng quan', tieude='Chuyên đề tổng tiền tố',
    mota='Năm kỹ thuật tổng tiền tố và lộ trình 50 bài luyện tập.'),
 'prefix-sum/1d/pre-hash/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tiền tố kết hợp bảng băm',
    tieude='Tiền tố kết hợp bảng băm',
    mota='Đếm đoạn con thỏa điều kiện bằng mảng cộng dồn và bảng băm.'),
 'prefix-sum/liarcnt.html': dict(
    cha=('Tổng tiền tố', 'index.html'), nhan='Quét trục số', tieude='Kỹ thuật quét trục số',
    mota='Nén tọa độ và quét sự kiện trên đường thẳng qua bài LIARCNT.'),
 'huffman/index.html': dict(
    nhom='Kỹ thuật', nhan='Thuật toán Huffman', tieude='Thuật toán Huffman và mã tiền tố',
    mota='Gộp hai đống nhẹ nhất để dựng mã tiền tố có tổng độ dài nhỏ nhất.'),
 'sieve/index.html': dict(
    nhom='Toán', nhan='Sàng nguyên tố', tieude='Sàng nguyên tố',
    mota='Sàng Eratosthenes và mảng ước nguyên tố nhỏ nhất.'),
 'in-exclusive/index.html': dict(
    nhom='Toán', nhan='Bao hàm — loại trừ', tieude='Bao hàm — loại trừ',
    mota='Đếm số phần tử thỏa ít nhất một trong nhiều điều kiện.'),
 'sols/index.html': dict(
    nhom='Bài luyện', nhan='Kho lời giải', tieude='Kho lời giải',
    mota='Toàn bộ trang hướng dẫn giải bài tập, xếp theo chuyên đề.'),

 # ---------- Lời giải: mảng 1 chiều ----------
 'array-1d/sols/ar2005/index.html': dict(
    cha=('Mảng 1 chiều', '../../index.html'), nhan='Tổng các đường chéo chính',
    tieude='Lời giải: Tổng các đường chéo chính',
    mota='Hướng dẫn giải bài Tổng các đường chéo chính (AR2005).'),
 'array-1d/sols/freqk/index.html': dict(
    cha=('Mảng 1 chiều', '../../index.html'), nhan='Giá trị thường xuyên',
    tieude='Lời giải: Giá trị thường xuyên',
    mota='Hướng dẫn giải bài Giá trị thường xuyên (FREQK).'),
 'sols/ar1010/index.html': dict(
    cha=('Mảng 1 chiều', '../../array-1d/index.html'), nhan='Phần tử thủ lĩnh',
    tieude='Lời giải: Phần tử thủ lĩnh',
    mota='Hướng dẫn giải bài Phần tử thủ lĩnh (AR1010).'),

 # ---------- Lời giải: mảng 2 chiều ----------
 'array-2d/arr2d_036/index.html': dict(
    cha=('Mảng 2 chiều', '../index.html'), nhan='Điểm mù của camera',
    tieude='Lời giải: Điểm mù của camera',
    mota='Hướng dẫn giải bài Điểm mù của camera (arr2d_036).'),
 'array-2d/arr2d_039/index.html': dict(
    cha=('Mảng 2 chiều', '../index.html'), nhan='Khu vực hỏa hoạn lớn nhất',
    tieude='Lời giải: Tìm khu vực hỏa hoạn lớn nhất',
    mota='Hướng dẫn giải bài Tìm khu vực hỏa hoạn lớn nhất (arr2d_039).'),
 'array-2d/arr2d_040/index.html': dict(
    cha=('Mảng 2 chiều', '../index.html'), nhan='Mảng hiệu số 2D',
    tieude='Lời giải: Mảng hiệu số 2D',
    mota='Hướng dẫn giải bài Mảng hiệu số hai chiều (arr2d_040).'),
 'array-2d/arr2d_047/index.html': dict(
    cha=('Mảng 2 chiều', '../index.html'), nhan='Tìm kiếm số hoàn hảo',
    tieude='Lời giải: Tìm kiếm số hoàn hảo',
    mota='Hướng dẫn giải bài Tìm kiếm số hoàn hảo (arr2d_047).'),

 # ---------- Lời giải: tổng tiền tố 1D ----------
 'prefix-sum/1d/differentarray_09/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Cộng cấp số cộng vào đoạn',
    tieude='Lời giải: Cộng cấp số cộng vào đoạn',
    mota='Hướng dẫn giải bài Cộng cấp số cộng vào đoạn (differentarray_09).'),
 'prefix-sum/1d/prefixsum_05/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tổng có trọng số',
    tieude='Lời giải: Tổng có trọng số',
    mota='Hướng dẫn giải bài Tổng có trọng số (prefixsum_05).'),
 # Mười bài của chương "Tối ưu nhờ tiền tố" — bản gốc ở
 # ChuyenDe/prefix-sum/05-toi-uu-nho-tien-to/, chép nguyên sang đây.
 'prefix-sum/1d/prefixsum_optimize/bai1-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Đoạn con tổng lớn nhất',
    tieude='Lời giải: Đoạn con tổng lớn nhất',
    mota='Hướng dẫn giải bài Đoạn con tổng lớn nhất.'),
 'prefix-sum/1d/prefixsum_optimize/bai2-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tổng lớn nhất, độ dài tối thiểu',
    tieude='Lời giải: Tổng lớn nhất với độ dài tối thiểu',
    mota='Hướng dẫn giải bài Tổng lớn nhất với độ dài tối thiểu.'),
 'prefix-sum/1d/prefixsum_optimize/bai3-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Xóa một phần tử để tổng lớn nhất',
    tieude='Lời giải: Xóa một phần tử để tổng lớn nhất',
    mota='Hướng dẫn giải bài Xóa một phần tử để tổng lớn nhất.'),
 'prefix-sum/1d/prefixsum_optimize/bai4-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Trung bình không nhỏ hơn X',
    tieude='Lời giải: Đoạn con dài nhất có trung bình không nhỏ hơn X',
    mota='Hướng dẫn giải bài Đoạn con dài nhất có trung bình không nhỏ hơn X.'),
 'prefix-sum/1d/prefixsum_optimize/bai5-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Hai đoạn con rời nhau',
    tieude='Lời giải: Hai đoạn con rời nhau tổng lớn nhất',
    mota='Hướng dẫn giải bài Hai đoạn con rời nhau tổng lớn nhất.'),
 'prefix-sum/1d/prefixsum_optimize/bai6-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tổng lớn nhất không vượt quá S',
    tieude='Lời giải: Đoạn con tổng lớn nhất không vượt quá S',
    mota='Hướng dẫn giải bài Đoạn con tổng lớn nhất không vượt quá S.'),
 'prefix-sum/1d/prefixsum_optimize/bai7-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tổng chia hết cho K',
    tieude='Lời giải: Đoạn con tổng lớn nhất chia hết cho K',
    mota='Hướng dẫn giải bài Đoạn con tổng lớn nhất chia hết cho K.'),
 'prefix-sum/1d/prefixsum_optimize/bai8-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Độ dài trong khoảng cho trước',
    tieude='Lời giải: Đoạn con tổng lớn nhất với độ dài trong khoảng',
    mota='Hướng dẫn giải bài Đoạn con tổng lớn nhất với độ dài trong khoảng cho trước.'),
 'prefix-sum/1d/prefixsum_optimize/bai9-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Chia đường gấp khúc cân bằng',
    tieude='Lời giải: Chia đường gấp khúc cân bằng',
    mota='Hướng dẫn giải bài Chia đường gấp khúc cân bằng.'),
 'prefix-sum/1d/prefixsum_optimize/bai10-sol.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Trung bình lớn nhất',
    tieude='Lời giải: Trung bình lớn nhất với độ dài tối thiểu',
    mota='Hướng dẫn giải bài Trung bình lớn nhất với độ dài tối thiểu.'),

 # ---------- Lời giải: tổng tiền tố 2D ----------
 'prefix-sum/2d/arr2d_015/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Đường đi của quân xe',
    tieude='Lời giải: Đường đi của quân xe với vật cản',
    mota='Hướng dẫn giải bài Đường đi của quân xe với vật cản (arr2d_015).'),
 'prefix-sum/2d/arr2d_020/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tám quân hậu',
    tieude='Lời giải: Tám quân hậu có tấn công nhau không',
    mota='Hướng dẫn giải bài Tám quân hậu có tấn công nhau không (arr2d_020).'),
 'prefix-sum/2d/prefixsum_2d_01/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Tổng hình chữ nhật con',
    tieude='Lời giải: Tổng hình chữ nhật con',
    mota='Hướng dẫn giải bài Tổng hình chữ nhật con (prefixsum_2d_01).'),
 'prefix-sum/2d/prefixsum_2d_05/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Đếm hình chữ nhật tổng bằng S',
    tieude='Lời giải: Đếm hình chữ nhật có tổng bằng S',
    mota='Hướng dẫn giải bài Đếm hình chữ nhật có tổng bằng S (prefixsum_2d_05).'),
 'prefix-sum/2d/prefixsum_2d_07/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Sự đa dạng của bức tranh',
    tieude='Lời giải: Sự đa dạng của bức tranh',
    mota='Hướng dẫn giải bài Sự đa dạng của bức tranh (prefixsum_2d_07).'),
 'prefix-sum/2d/prefixsum_2d_09/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Vùng phủ dày đặc nhất',
    tieude='Lời giải: Vùng phủ dày đặc nhất',
    mota='Hướng dẫn giải bài Vùng phủ dày đặc nhất (prefixsum_2d_09).'),
 'prefix-sum/2d/prefixsum_2d_11/index.html': dict(
    cha=('Tổng tiền tố', '../../index.html'), nhan='Hình chữ nhật chia hết cho K',
    tieude='Lời giải: Đếm hình chữ nhật chia hết cho K',
    mota='Hướng dẫn giải bài Đếm hình chữ nhật chia hết cho K (prefixsum_2d_11).'),

 # ---------- Lời giải: cây ----------
 'tree/viet_lvl3_106/index.html': dict(
    cha=('Cây & LCA', '../index.html'), nhan='Tối ưu điểm họp làng',
    tieude='Lời giải: Tối ưu điểm họp làng (Rerooting DP)',
    mota='Hướng dẫn giải bài Tối ưu điểm họp làng bằng kỹ thuật đổi gốc.'),
 'tree/viet_lvl4_090/index.html': dict(
    cha=('Cây & LCA', '../index.html'), nhan='Tích số trên đường đi',
    tieude='Lời giải: Kiểm tra tích số trên đường đi',
    mota='Hướng dẫn giải bài Kiểm tra tích số trên đường đi (viet_lvl4_090).'),
 'tree/sols/viet_lvl4_122/index.html': dict(
    cha=('Cây & LCA', '../../index.html'), nhan='Ước nguyên tố trên đường đi',
    tieude='Lời giải: Đếm số ước nguyên tố trên đường đi',
    mota='Hướng dẫn giải bài Đếm số ước nguyên tố trên đường đi (viet_lvl4_122).'),
 'tree/sols/viet_lvl4_257/index.html': dict(
    cha=('Cây & LCA', '../../index.html'), nhan='Hái táo',
    tieude='Lời giải: Hái táo',
    mota='Hướng dẫn giải bài Hái táo (viet_lvl4_257).'),

 # ---------- Lời giải: quy hoạch động ----------
 'dp/range/viet_lvl4_1680/index.html': dict(
    cha=('Quy hoạch động', '../../index.html'), nhan='Hợp nhất các đống sỏi',
    tieude='Lời giải: Hợp nhất các đống sỏi',
    mota='Hướng dẫn giải bài Hợp nhất các đống sỏi bằng quy hoạch động trên đoạn.'),

 # ---------- Lời giải: đề HSG 12 ----------
 'sols/2627_hsg12_c1p1/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Cước vận chuyển',
    tieude='Lời giải: Cước vận chuyển',
    mota='Hướng dẫn giải bài Cước vận chuyển, đề HSG 12 năm 2627 câu 1.'),
 'sols/2627_hsg12_c1p2/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Ghép thẻ số',
    tieude='Lời giải: Ghép thẻ số',
    mota='Hướng dẫn giải bài Ghép thẻ số, đề HSG 12 năm 2627 câu 1.'),
 'sols/2627_hsg12_c1p3/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Đoạn chia hết',
    tieude='Lời giải: Đoạn chia hết',
    mota='Hướng dẫn giải bài Đoạn chia hết, đề HSG 12 năm 2627 câu 1.'),
 'sols/2627_hsg12_c1p4/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Đảo chiều đường một chiều',
    tieude='Lời giải: Đảo chiều đường một chiều',
    mota='Hướng dẫn giải bài Đảo chiều đường một chiều, đề HSG 12 năm 2627 câu 1.'),

 # ---------- Lời giải: bài luyện khác ----------
 'sols/ki_chuyentuyen/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Chi phí chuyển tuyến',
    tieude='Lời giải: Chi phí chuyển tuyến',
    mota='Hướng dẫn giải bài Chi phí chuyển tuyến.'),
 'sols/th5_b_21d_903fc/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Bảng quảng cáo',
    tieude='Lời giải: Bảng quảng cáo',
    mota='Hướng dẫn giải bài Bảng quảng cáo.'),
 'sols/th5_d_2d_732fc/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Phân rã cây',
    tieude='Lời giải: Phân rã cây',
    mota='Hướng dẫn giải bài Phân rã cây.'),
 'sols/th5_d_myg_979101fc/index.html': dict(
    cha=('Kho lời giải', '../index.html'), nhan='Tổng độ đơn điệu',
    tieude='Lời giải: Tổng độ đơn điệu',
    mota='Hướng dẫn giải bài Tổng độ đơn điệu.'),
}

# Trang có thanh mục lục cố định bên trái: thanh điều hướng phải nằm trong
# cột nội dung, và chân trang phải né vùng thanh bên.
CO_THANH_BEN = {
    'array-1d/index.html',
    'array-2d/index.html',
    'dsu/index.html',
    'euler-circuit/index.html',
    'huffman/index.html',
    'in-exclusive/index.html',
    'io/index.html',
    'prefix-sum/1d/index.html',
    'prefix-sum/1d/pre-hash/index.html',
    'prefix-sum/1d/prefixsum_optimize/bai1-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai10-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai2-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai3-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai4-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai5-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai6-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai7-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai8-sol.html',
    'prefix-sum/1d/prefixsum_optimize/bai9-sol.html',
    'prefix-sum/liarcnt.html',
    'prefix-sum/prefix-sum-1d/index.html',
    'sieve/index.html',
    'sqrt-decomposition/index.html',
    'string/index.html',
    'tree/euler-tour/index.html',
    'tree/index.html',
}
# Trang không có thanh bên nhưng nội dung nằm trong <div class="wrap">.
TRONG_WRAP = CO_THANH_BEN | {'euler-circuit/index.html'}

TEN_SITE = 'Lý thuyết CP'

# =====================================================================
#  Tiện ích
# =====================================================================

def tim_the_dong(text, i, tag):
    """Trả về vị trí ngay sau </tag> khớp với thẻ mở bắt đầu tại i (đếm lồng nhau)."""
    mo = re.compile(r'<\s*' + tag + r'\b', re.I)
    dong = re.compile(r'<\s*/\s*' + tag + r'\s*>', re.I)
    sau = text.index('>', i) + 1
    sau_khi_mo = text[i:sau]
    if sau_khi_mo.rstrip().endswith('/>'):
        return sau
    muc = 1
    vt = sau
    while muc > 0:
        m1 = mo.search(text, vt)
        m2 = dong.search(text, vt)
        if not m2:
            raise ValueError(f'khong tim thay </{tag}>')
        if m1 and m1.start() < m2.start():
            muc += 1
            vt = m1.end()
        else:
            muc -= 1
            vt = m2.end()
    return vt


def go_khoi(text, mo_dau, ket_thuc):
    """Gỡ mọi khối nằm giữa hai chú thích mốc (để chạy lại được nhiều lần)."""
    while True:
        i = text.find(mo_dau)
        if i < 0:
            return text
        j = text.find(ket_thuc, i)
        if j < 0:
            return text
        text = text[:i] + text[j + len(ket_thuc):]
        text = re.sub(r'\n{3,}', '\n\n', text)


def lop_cua(the_mo):
    m = re.search(r'class\s*=\s*"([^"]*)"', the_mo, re.I)
    return m.group(1).split() if m else []


def la_thanh_dieu_huong(khoi):
    """Chỉ coi là thanh điều hướng khi khối có liên kết về trang chủ hoặc sang
    judge. Ba trang dùng chính lớp `topbar` cho thanh điều khiển mô phỏng
    (Reset / Lùi / Tiến) — những thanh đó chỉ có <button> nên không dính bẫy.
    Mục lục trong <nav> cũng không dính, vì nó chỉ trỏ tới neo #... trong trang."""
    return bool(re.search(r'href\s*=\s*"[^"]*index\.html"', khoi, re.I)
                or 'cvpoi.id.vn' in khoi)


def go_dieu_huong_cu(text):
    """Gỡ thanh điều hướng cũ dù nó viết theo kiểu nào, và gỡ liên kết
    'Trang chủ' chèn tay ở đợt trước. Trả về (văn bản mới, số khối đã gỡ)."""
    so = 0

    for tag, dieu_kien in (('div', lambda l: 'topbar' in l),
                           ('nav', lambda l: 'toc' not in l and 'muc' not in l)):
        vt = 0
        while True:
            m = re.search(r'<' + tag + r'\b[^>]*>', text[vt:], re.I)
            if not m:
                break
            dau = vt + m.start()
            if not dieu_kien(lop_cua(m.group(0))):
                vt = dau + len(m.group(0))
                continue
            het = tim_the_dong(text, dau, tag)
            khoi = text[dau:het]
            if not la_thanh_dieu_huong(khoi):
                vt = dau + len(m.group(0))
                continue
            text = text[:dau] + text[het:]
            so += 1
            vt = dau

    # Liên kết "← Trang chủ" chèn tay ở đợt 1
    text, n = re.subn(
        r'[ \t]*<a href="[^"]*"[^>]*style="display:inline-flex;[^"]*currentColor[^"]*"[^>]*>[^<]*</a>\s*\n',
        '', text)
    so += n

    return text, so


def go_chan_trang_cu(text):
    so = 0
    while True:
        m = re.search(r'<footer\b[^>]*>', text, re.I)
        if not m:
            return text, so
        het = tim_the_dong(text, m.start(), 'footer')
        text = text[:m.start()] + text[het:]
        so += 1


def e(s):
    return html.escape(s, quote=True)


def dung_head(pfx, tieude, mota):
    td = f'{tieude} | {TEN_SITE}' if tieude != TEN_SITE else f'{TEN_SITE} — Thầy Việt'
    return (
        '<!--cv-head-->\n'
        f'<link rel="stylesheet" href="{pfx}assets/site.css">\n'
        f'<link rel="icon" type="image/svg+xml" href="{pfx}assets/favicon.svg">\n'
        f'<meta name="description" content="{e(mota)}">\n'
        '<meta property="og:type" content="article">\n'
        f'<meta property="og:site_name" content="{e(TEN_SITE)}">\n'
        f'<meta property="og:title" content="{e(td)}">\n'
        f'<meta property="og:description" content="{e(mota)}">\n'
        '<!--/cv-head-->'
    )


ICON_NHA = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>')
ICON_SACH = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
             '<path d="M4 5h16v14H4z"/><path d="M8 9h8M8 13h5"/></svg>')
ICON_CAU = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
            '<path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/></svg>')


def dung_nav(pfx, tt):
    """Dựng thanh điều hướng. pfx là chuỗi ../ đưa về thư mục gốc."""
    nha = pfx + 'index.html'
    kho = pfx + 'sols/index.html'
    vun = []
    if tt.get('cha'):
        nhan_cha, href_cha = tt['cha']
        vun.append(f'<a href="{href_cha}">{e(nhan_cha)}</a>')
    elif tt.get('nhom'):
        vun.append(e(tt['nhom']))
    if tt.get('nhan'):
        vun.append(f'<span class="cv-here">{e(tt["nhan"])}</span>')
    crumb = '<span class="cv-sep">/</span>'.join(vun)

    # Nhãn bọc trong <span> để màn hình hẹp giấu chữ, chỉ chừa biểu tượng.
    nut_nha = '' if pfx == '' and not tt.get('nhan') else (
        f'<a class="cv-btn" href="{nha}">{ICON_NHA}<span>Trang chủ</span></a>')
    nut_kho = (f'<a class="cv-btn cv-phu" href="{kho}" title="Kho lời giải">'
               f'{ICON_SACH}<span>Kho lời giải</span></a>')
    nut_judge = (f'<a class="cv-btn cv-phu" href="https://cvpoi.id.vn" target="_blank" '
                 f'rel="noopener" title="cvpoi.id.vn">{ICON_CAU}<span>cvpoi.id.vn</span></a>')

    return (
        '<!--cv-nav-->\n'
        '<nav class="cv-nav">\n  <div class="cv-nav-in">\n    '
        + ''.join(x for x in [nut_nha, nut_kho, nut_judge] if x)
        + (f'\n    <span class="cv-crumb">{crumb}</span>' if crumb else '')
        + '\n  </div>\n</nav>\n<!--/cv-nav-->'
    )


def dung_footer(pfx):
    nha = pfx + 'index.html'
    return (
        '<!--cv-foot-->\n'
        '<footer class="cv-footer">\n'
        '  <span>&copy; <b>Phan Văn Việt</b> — THPT Chuyên Vĩnh Phúc '
        '&middot; Chuyên đề lập trình thi đấu</span>\n'
        f'  <span>SĐT 0987072896 &middot; <a href="{nha}">Trang chủ</a> '
        '&middot; <a href="https://cvpoi.id.vn" target="_blank" rel="noopener">cvpoi.id.vn</a></span>\n'
        '</footer>\n<!--/cv-foot-->'
    )


def them_lop_body(text, lop):
    m = re.search(r'<body\b([^>]*)>', text, re.I)
    if not m:
        return text
    thuoc_tinh = m.group(1)
    if re.search(r'\bclass\s*=', thuoc_tinh, re.I):
        if lop in thuoc_tinh:
            return text
        moi = re.sub(r'(class\s*=\s*")', r'\1' + lop + ' ', thuoc_tinh, count=1, flags=re.I)
    else:
        moi = thuoc_tinh + f' class="{lop}"'
    return text[:m.start()] + f'<body{moi}>' + text[m.end():]


# =====================================================================
#  Chạy
# =====================================================================

def xu_ly(duong_dan_tuong_doi, tt, ghi):
    p = os.path.join(ROOT, duong_dan_tuong_doi.replace('/', os.sep))
    goc = open(p, encoding='utf-8').read()
    text = goc

    sau = len(duong_dan_tuong_doi.split('/')) - 1
    pfx = '../' * sau

    # 1. Gỡ mọi thứ do lần chạy trước sinh ra
    for a, b in (('<!--cv-head-->', '<!--/cv-head-->'),
                 ('<!--cv-nav-->', '<!--/cv-nav-->'),
                 ('<!--cv-foot-->', '<!--/cv-foot-->')):
        text = go_khoi(text, a, b)

    # 2. Gỡ thanh điều hướng cũ và chân trang cũ
    text, so_nav = go_dieu_huong_cu(text)
    text, so_ft = go_chan_trang_cu(text)

    # 3. Gỡ thẻ mô tả / og / favicon trang tự khai, rồi chèn khối <head> chuẩn.
    #    (Không gỡ thì trang nào vốn đã có description sẽ bị khai hai lần.)
    text = re.sub(r'[ \t]*<meta\s+name\s*=\s*"description"[^>]*>\s*\n?', '', text, flags=re.I)
    text = re.sub(r'[ \t]*<meta\s+property\s*=\s*"og:[^"]*"[^>]*>\s*\n?', '', text, flags=re.I)
    text = re.sub(r'[ \t]*<link\s+[^>]*rel\s*=\s*"(?:shortcut )?icon"[^>]*>\s*\n?', '', text, flags=re.I)
    text = text.replace('</head>', dung_head(pfx, tt['tieude'], tt['mota']) + '\n</head>', 1)

    # 4. Chuẩn hóa <title>
    td = (f"{tt['tieude']} | {TEN_SITE}" if tt['tieude'] != TEN_SITE
          else f'{TEN_SITE} — Thầy Việt')
    text = re.sub(r'<title>.*?</title>', lambda _: f'<title>{e(td)}</title>',
                  text, count=1, flags=re.S)

    # 5. Lớp cho trang có thanh bên
    if duong_dan_tuong_doi in CO_THANH_BEN:
        text = them_lop_body(text, 'cv-side')

    # 6. Chèn thanh điều hướng
    nav = dung_nav(pfx, tt)
    m_wrap = (re.search(r'<div[^>]*\bclass\s*=\s*"[^"]*\bwrap\b[^"]*"[^>]*>', text, re.I)
              if duong_dan_tuong_doi in TRONG_WRAP else None)
    if m_wrap:
        # Trang có cột nội dung riêng: thanh điều hướng phải nằm trong cột đó,
        # nếu không nó sẽ chui xuống dưới thanh mục lục cố định bên trái.
        text = text[:m_wrap.end()] + '\n' + nav + text[m_wrap.end():]
    else:
        m = re.search(r'<body\b[^>]*>', text, re.I)
        text = text[:m.end()] + '\n' + nav + text[m.end():]

    # 7. Chèn chân trang
    text = text.replace('</body>', dung_footer(pfx) + '\n</body>', 1)

    text = re.sub(r'\n{3,}', '\n\n', text)
    thay_doi = text != goc
    if ghi and thay_doi:
        open(p, 'w', encoding='utf-8', newline='').write(text)
    return so_nav, so_ft, thay_doi


def main():
    ghi = '--ghi' in sys.argv
    tong_nav = tong_ft = tong_doi = 0
    loi = []
    for duong_dan, tt in TRANG.items():
        p = os.path.join(ROOT, duong_dan.replace('/', os.sep))
        if not os.path.isfile(p):
            loi.append(f'THIEU FILE: {duong_dan}')
            continue
        try:
            a, b, c = xu_ly(duong_dan, tt, ghi)
        except Exception as ex:
            loi.append(f'{duong_dan}: {ex}')
            continue
        tong_nav += a
        tong_ft += b
        tong_doi += 1 if c else 0

    # Trang có trên đĩa mà chưa khai trong TRANG
    tren_dia = set()
    for dp, dn, fn in os.walk(ROOT):
        if '.git' in dp.split(os.sep):
            continue
        for f in fn:
            if f.lower().endswith('.html'):
                tren_dia.add(os.path.relpath(os.path.join(dp, f), ROOT).replace('\\', '/'))
    thieu_khai = sorted(tren_dia - set(TRANG))

    print(('DA GHI' if ghi else 'XEM TRUOC (chua ghi gi)'))
    print(f'  Trang da khai              : {len(TRANG)}')
    print(f'  Trang thuc su doi noi dung : {tong_doi}')
    print(f'  Thanh dieu huong cu da go  : {tong_nav}')
    print(f'  Chan trang cu da go        : {tong_ft}')
    print(f'  Trang chua khai trong TRANG: {len(thieu_khai)}')
    for t in thieu_khai:
        print(f'      {t}')
    if loi:
        print(f'  LOI ({len(loi)}):')
        for l in loi:
            print(f'      {l}')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
