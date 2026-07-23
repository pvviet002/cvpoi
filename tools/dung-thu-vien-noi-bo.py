# -*- coding: utf-8 -*-
"""
dung-thu-vien-noi-bo.py — chuyển mọi trang từ gọi thư viện qua CDN sang dùng
bản đã tải về assets/.

Chạy TRƯỚC (một lần, cần mạng):
    curl -sSL -o assets/html2canvas.min.js https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js
    # (PowerShell: Invoke-WebRequest -Uri "...same URL..." -OutFile "assets/html2canvas.min.js")

Rồi:
    python tools/dung-thu-vien-noi-bo.py          # xem trước
    python tools/dung-thu-vien-noi-bo.py --ghi    # ghi thật

Công cụ TỰ quét mọi trang HTML, tìm thẻ <script> trỏ tới cdnjs/jsdelivr rồi đổi
sang bản nội bộ, tự tính số ../ theo độ sâu của trang. Chạy lại được nhiều lần.

Vì sao MathJax (nếu có) lấy bản tex-mml-svg: bản chtml lúc chạy còn tải thêm ~30
file phông, chép mỗi file JS về là hiện sai phông. Hiện site đã bỏ hẳn MathJax
ở liarcnt (công thức viết bằng HTML thuần), nên nhánh MathJax chỉ để dự phòng.
"""

import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (mẫu URL trên CDN, tên file trong assets/, có bắt buộc phải tồn tại không)
NGUON = [
    (re.compile(r'https://cdnjs\.cloudflare\.com/ajax/libs/html2canvas/[^"\']*'),
     'html2canvas.min.js', True),
    (re.compile(r'https://cdn\.jsdelivr\.net/npm/mathjax@3/es5/tex-mml-[a-z-]+\.js'),
     'mathjax-tex-svg.js', False),
]


def sau_cua(rel):
    return rel.replace('\\', '/').count('/')


def main():
    ghi = '--ghi' in sys.argv

    # Chỉ đòi có file cho những nguồn thực sự đang được trang nào đó dùng.
    dang_dung = set()
    trang = []
    for dp, dn, fn in os.walk(ROOT):
        if '.git' in dp.split(os.sep) or dp.endswith('assets'):
            continue
        for f in fn:
            if f.lower().endswith('.html'):
                p = os.path.join(dp, f)
                t = open(p, encoding='utf-8', errors='replace').read()
                dùng = [asset for rx, asset, _ in NGUON if rx.search(t)]
                if dùng:
                    trang.append((p, os.path.relpath(p, ROOT).replace(os.sep, '/')))
                    dang_dung.update(dùng)

    thiếu = [a for a in dang_dung if not os.path.isfile(os.path.join(ROOT, 'assets', a))]
    if thiếu:
        print('CHUA CO cac file sau trong assets/ — hay tai ve truoc:')
        for a in thiếu:
            print('   ', a)
        return 1

    tong = 0
    for p, rel in sorted(trang, key=lambda x: x[1]):
        t = open(p, encoding='utf-8').read()
        goc = t
        pfx = '../' * sau_cua(rel)
        for rx, asset, _ in NGUON:
            t = rx.sub(pfx + 'assets/' + asset, t)
        con = len(re.findall(r'cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net', t))
        if t != goc:
            tong += 1
            if ghi:
                open(p, 'w', encoding='utf-8', newline='').write(t)
        print(f'  {rel:50s} {"da doi" if t != goc else "khong doi":9s} con goi CDN: {con}')

    print(('DA GHI' if ghi else 'XEM TRUOC (chua ghi gi)') + f' — {tong} trang')
    return 0


if __name__ == '__main__':
    sys.exit(main())
