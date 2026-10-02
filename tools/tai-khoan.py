# -*- coding: utf-8 -*-
"""
tai-khoan.py — quản lý tài khoản đăng nhập của site (tệp _auth/taikhoan.js)
và soát luật xem trang (tệp _auth/quyen.js).

Chạy từ thư mục gốc của repo:

    python tools/tai-khoan.py them an.nv --ten "Nguyễn Văn An" --nhom hsg9
    python tools/tai-khoan.py nhap lop9.csv        # thêm cả lớp từ tệp CSV
    python tools/tai-khoan.py ds                   # liệt kê tài khoản
    python tools/tai-khoan.py doi-nhom an.nv --nhom hsg9,hsg12
    python tools/tai-khoan.py dat-lai an.nv        # cấp mật khẩu mới
    python tools/tai-khoan.py xoa an.nv
    python tools/tai-khoan.py quyen                # trang nào mở, trang nào khoá

Mật khẩu do công cụ sinh ngẫu nhiên và CHỈ IN MỘT LẦN (tệp chỉ lưu mã băm);
muốn tự đặt thì thêm --mk "...". Mọi thay đổi có hiệu lực trên web sau khi
git commit + git push (Vercel deploy lại, khoảng một phút).

Tệp CSV cho lệnh `nhap`: mỗi dòng  tên-đăng-nhập,Họ tên,nhóm  (nhiều nhóm
cách nhau bằng dấu chấm phẩy), UTF-8, không cần dòng tiêu đề. Mật khẩu vừa
cấp được ghi ra  <tên-tệp>.matkhau.csv  cạnh tệp CSV để in phát cho học sinh
(đuôi này đã nằm trong .gitignore, không bị đưa lên GitHub).

Nhóm đặc biệt: "giaovien" xem được mọi trang.
"""

import argparse, csv, hashlib, json, os, re, secrets, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEP_TK = os.path.join(ROOT, '_auth', 'taikhoan.js')
TEP_QUYEN = os.path.join(ROOT, '_auth', 'quyen.js')

VONG = 100000                     # phải khớp cách băm trong middleware.js
TOAN_QUYEN = 'giaovien'
MOC = 'export default'
# Bỏ các ký tự dễ đọc nhầm khi chép tay: 0/O, 1/l/I.
BANG_CHU = 'abcdefghjkmnpqrstuvwxyz23456789'

DAU_TEP = (
    '/* Danh sách tài khoản — do tools/tai-khoan.py sinh, ĐỪNG sửa tay.\n'
    '   Mật khẩu chỉ lưu dạng băm (PBKDF2-SHA256 kèm muối), không khôi phục lại được.\n'
    '   Thêm / xoá / đổi nhóm / đặt lại mật khẩu: python tools/tai-khoan.py --help */\n'
)


def doc_js(tep):
    """Đọc phần JSON đứng sau `export default` của một tệp trong _auth/."""
    text = open(tep, encoding='utf-8').read()
    # Mốc phải đứng đầu dòng: phần chú thích đầu tệp cũng nhắc tới cụm này.
    i = re.search(r'^' + MOC, text, re.M).end()
    return json.loads(text[i:].strip().rstrip(';'))


def ghi_tk(ds):
    than = json.dumps(dict(sorted(ds.items())), ensure_ascii=False, indent=1)
    with open(TEP_TK, 'w', encoding='utf-8', newline='\n') as f:
        f.write(DAU_TEP + MOC + ' ' + than + ';\n')


def bam(mat_khau, muoi_hex):
    return hashlib.pbkdf2_hmac('sha256', mat_khau.encode('utf-8'),
                               bytes.fromhex(muoi_hex), VONG, 32).hex()


def sinh_mat_khau():
    return ''.join(secrets.choice(BANG_CHU) for _ in range(10))


def chuan_ten(ten):
    ten = ten.strip().lower()
    if not re.fullmatch(r'[a-z0-9][a-z0-9._-]{1,31}', ten):
        sys.exit(f'Tên đăng nhập "{ten}" không hợp lệ: chỉ dùng chữ thường không dấu, '
                 'số, dấu chấm, gạch nối, gạch dưới; dài 2–32 ký tự.')
    return ten


def tach_nhom(s):
    nhom = [x.strip().lower() for x in re.split(r'[;,]', s) if x.strip()]
    for n in nhom:
        if not re.fullmatch(r'[a-z0-9_-]+', n) or n in ('mo',):
            sys.exit(f'Tên nhóm "{n}" không hợp lệ.')
    if not nhom:
        sys.exit('Phải có ít nhất một nhóm.')
    return nhom


def tao_muc(ho_ten, nhom, mat_khau):
    muoi = secrets.token_hex(16)
    return {'ten': ho_ten, 'nhom': nhom, 'muoi': muoi, 'vong': VONG, 'bam': bam(mat_khau, muoi)}


def canh_bao_nhom(nhom):
    """Nhóm chưa xuất hiện trong luật nào thì nhiều khả năng là gõ nhầm."""
    co = {TOAN_QUYEN}
    for l in doc_js(TEP_QUYEN):
        co.update(l['nhom'])
    la = [n for n in nhom if n not in co]
    if la:
        print(f'  (lưu ý: nhóm {", ".join(la)} chưa có trong luật nào của _auth/quyen.js)')


def nhac_push():
    print('Nhớ git commit + git push để thay đổi có hiệu lực trên web.')


# ---------------------------------------------------------------- các lệnh

def lenh_them(a):
    ds = doc_js(TEP_TK)
    ten = chuan_ten(a.tai_khoan)
    if ten in ds:
        sys.exit(f'Tài khoản "{ten}" đã có. Dùng dat-lai / doi-nhom, hoặc xoa rồi thêm lại.')
    nhom = tach_nhom(a.nhom)
    mk = a.mk or sinh_mat_khau()
    ds[ten] = tao_muc(a.ten or ten, nhom, mk)
    ghi_tk(ds)
    print(f'Đã thêm: {ten}  ({ds[ten]["ten"]})  nhóm: {", ".join(nhom)}')
    if not a.mk:
        print(f'Mật khẩu: {mk}     <- chỉ hiện lần này')
    canh_bao_nhom(nhom)
    nhac_push()


def lenh_nhap(a):
    ds = doc_js(TEP_TK)
    moi, bo_qua = [], []
    with open(a.tep, encoding='utf-8-sig', newline='') as f:
        for dong in csv.reader(f):
            dong = [x.strip() for x in dong]
            if not dong or not dong[0] or dong[0].startswith('#'):
                continue
            if len(dong) < 3:
                sys.exit(f'Dòng thiếu cột (cần: tên-đăng-nhập,Họ tên,nhóm): {dong}')
            ten = chuan_ten(dong[0])
            if ten in ds:
                bo_qua.append(ten)
                continue
            nhom = tach_nhom(dong[2])
            mk = sinh_mat_khau()
            ds[ten] = tao_muc(dong[1] or ten, nhom, mk)
            moi.append((ten, dong[1], ';'.join(nhom), mk))
    if moi:
        ghi_tk(ds)
        tep_mk = os.path.splitext(a.tep)[0] + '.matkhau.csv'
        with open(tep_mk, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Tên đăng nhập', 'Họ tên', 'Nhóm', 'Mật khẩu'])
            w.writerows(moi)
        print(f'Đã thêm {len(moi)} tài khoản. Mật khẩu ghi ở: {tep_mk}')
    if bo_qua:
        print(f'Bỏ qua {len(bo_qua)} tên đã có: {", ".join(bo_qua)}')
    if moi:
        nhac_push()


def lenh_ds(a):
    ds = doc_js(TEP_TK)
    if not ds:
        print('Chưa có tài khoản nào.')
        return
    rong = max(len(t) for t in ds)
    for ten, tk in sorted(ds.items(), key=lambda kv: (kv[1]['nhom'], kv[0])):
        print(f'  {ten:<{rong}}  {", ".join(tk["nhom"]):<18}  {tk["ten"]}')
    print(f'Tổng: {len(ds)} tài khoản.')


def lay(ds, ten):
    ten = ten.strip().lower()
    if ten not in ds:
        sys.exit(f'Không có tài khoản "{ten}".')
    return ten


def lenh_doi_nhom(a):
    ds = doc_js(TEP_TK)
    ten = lay(ds, a.tai_khoan)
    ds[ten]['nhom'] = tach_nhom(a.nhom)
    ghi_tk(ds)
    print(f'{ten}: nhóm mới là {", ".join(ds[ten]["nhom"])}')
    canh_bao_nhom(ds[ten]['nhom'])
    nhac_push()


def lenh_dat_lai(a):
    ds = doc_js(TEP_TK)
    ten = lay(ds, a.tai_khoan)
    mk = a.mk or sinh_mat_khau()
    cu = ds[ten]
    ds[ten] = tao_muc(cu['ten'], cu['nhom'], mk)
    ghi_tk(ds)
    print(f'Đã đặt lại mật khẩu cho {ten}. Phiên đăng nhập cũ của tài khoản này hết hiệu lực.')
    if not a.mk:
        print(f'Mật khẩu: {mk}     <- chỉ hiện lần này')
    nhac_push()


def lenh_xoa(a):
    ds = doc_js(TEP_TK)
    ten = lay(ds, a.tai_khoan)
    del ds[ten]
    ghi_tk(ds)
    print(f'Đã xoá {ten}.')
    nhac_push()


def chuan_hoa(p):
    """Bản Python của hàm chuanHoa + timLuat trong middleware.js."""
    p = p.lower()
    if p.endswith('/index.html'):
        p = p[:-len('index.html')]
    return p


def tim_luat(luat, p):
    tot, dai = None, -1
    for l in luat:
        d = l['duong'].lower()
        trung = p == d or p + '/' == d
        if l.get('chinhxac'):
            if trung:
                return l
            continue
        if (trung or p.startswith(d)) and len(d) > dai:
            tot, dai = l, len(d)
    return tot


def lenh_quyen(a):
    luat = doc_js(TEP_QUYEN)
    trang = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in ('.git', '_auth', 'tools', 'assets', '__pycache__')]
        for f in fn:
            if f.lower().endswith('.html'):
                trang.append('/' + os.path.relpath(os.path.join(dp, f), ROOT).replace('\\', '/'))
    theo_muc = {}
    da_dung = set()
    for t in sorted(trang):
        l = tim_luat(luat, chuan_hoa(t))
        if l is None or 'mo' in l['nhom']:
            muc = 'MỞ (không cần đăng nhập)'
        elif '*' in l['nhom']:
            muc = 'Có tài khoản là xem được'
        else:
            muc = 'Chỉ nhóm: ' + ', '.join(l['nhom'])
        if l is not None:
            da_dung.add(id(l))
        theo_muc.setdefault(muc, []).append(t)
    for muc in sorted(theo_muc):
        ds = theo_muc[muc]
        print(f'\n{muc} — {len(ds)} trang')
        if muc.startswith('MỞ') and not a.day_du:
            # Trang mở rất nhiều; gom theo thư mục cấp một cho dễ soát.
            goc = sorted({t.split('/')[1] for t in ds})
            print('  ' + ', '.join(goc))
            print('  (thêm --day-du để liệt kê từng trang)')
        else:
            for t in ds:
                print('  ' + t)
    thua = [l['duong'] for l in luat if id(l) not in da_dung]
    if thua:
        print('\nLuật không khớp trang nào (gõ nhầm đường dẫn?): ' + ', '.join(thua))


def main():
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, 'reconfigure'):
            luong.reconfigure(encoding='utf-8')
    p = argparse.ArgumentParser(description='Quản lý tài khoản đăng nhập của site.')
    sub = p.add_subparsers(dest='lenh', required=True)

    s = sub.add_parser('them', help='thêm một tài khoản')
    s.add_argument('tai_khoan')
    s.add_argument('--ten', help='họ tên hiển thị')
    s.add_argument('--nhom', required=True, help='một hay nhiều nhóm, cách nhau dấu phẩy')
    s.add_argument('--mk', help='tự đặt mật khẩu (bỏ trống thì sinh ngẫu nhiên)')
    s.set_defaults(ham=lenh_them)

    s = sub.add_parser('nhap', help='thêm nhiều tài khoản từ tệp CSV')
    s.add_argument('tep')
    s.set_defaults(ham=lenh_nhap)

    s = sub.add_parser('ds', help='liệt kê tài khoản')
    s.set_defaults(ham=lenh_ds)

    s = sub.add_parser('doi-nhom', help='đổi nhóm của một tài khoản')
    s.add_argument('tai_khoan')
    s.add_argument('--nhom', required=True)
    s.set_defaults(ham=lenh_doi_nhom)

    s = sub.add_parser('dat-lai', help='cấp mật khẩu mới')
    s.add_argument('tai_khoan')
    s.add_argument('--mk')
    s.set_defaults(ham=lenh_dat_lai)

    s = sub.add_parser('xoa', help='xoá một tài khoản')
    s.add_argument('tai_khoan')
    s.set_defaults(ham=lenh_xoa)

    s = sub.add_parser('quyen', help='soát luật: trang nào mở, trang nào khoá')
    s.add_argument('--day-du', action='store_true', help='liệt kê cả từng trang mở')
    s.set_defaults(ham=lenh_quyen)

    a = p.parse_args()
    a.ham(a)


if __name__ == '__main__':
    main()
