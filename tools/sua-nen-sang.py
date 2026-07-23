# -*- coding: utf-8 -*-
"""
sua-nen-sang.py — sửa lỗi tương phản ở nền sáng cho các trang đã theo chuẩn.

Nguyên nhân: từng trang có màu gõ cứng của bản nền tối (nền hộp tối, chữ cú
pháp sáng, chữ nội dung sáng) không đổi theo nút chuyển nền. Công cụ thêm một
khối CSS ở CUỐI <style> mỗi trang, ép các lớp đó về bảng màu của chuẩn (biến
--card / --fg / --code-bg / token màu) vốn tự đổi theo nền sáng/tối.

    python tools/sua-nen-sang.py          # xem trước
    python tools/sua-nen-sang.py --ghi    # ghi thật

Chạy lại được nhiều lần: khối chèn được bọc trong mốc /*cv-fix-*/.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOC_DAU = '/*cv-fix-nen-sang*/'
MOC_CUOI = '/*/cv-fix-nen-sang*/'

KHOI = MOC_DAU + """
/* Ép mọi màu gõ cứng của bản nền tối theo bảng màu của chuẩn (tự đổi theo
   nền sáng/tối). Đặt cuối <style> nên thắng các quy tắc trước cùng độ đặc hiệu. */

/* 0) Màu chú thích mã mặc định của chuẩn (#8b949e) quá nhạt trên nền sáng
   (tương phản 2,89 < 4,5). Làm đậm hơn ở nền sáng, giữ nguyên ở nền tối.
   Khối <style> này đứng SAU chuan.css nên đè được cả bốn trạng thái nền. */
:root{--c-cmt:#5f6672}
@media (prefers-color-scheme:dark){:root{--c-cmt:#8b949e}}
:root[data-theme="light"]{--c-cmt:#5f6672}
:root[data-theme="dark"]{--c-cmt:#8b949e}

/* 1) Khối mã tự tạo của trang: nền và chữ theo chuẩn, rồi token màu cú pháp
      dùng bảng token của chuẩn (var --c-*) vốn tự đổi nền. */
/* KHÔNG đụng .codeline: nó có biến thể .codeline.hot tô sáng dòng đang chạy,
   ép nền sẽ xoá mất hiệu ứng đó. Chỉ ép khung chứa và màu chữ mặc định. */
.code-block, .code-container, .code, .code-runner, pre.code-block{
  background:var(--code-bg) !important;
}
.code-block, .code-container, .code, .code-runner, pre.code-block, .codeline{
  color:var(--code-fg) !important;
}
.c-kw,.tk-keyword,.kw,.token-kw{color:var(--c-kw) !important}
.c-str,.tk-string,.st,.token-str{color:var(--c-str) !important}
.c-cm,.tk-comment,.cm,.token-com{color:var(--c-cmt) !important}
.c-num,.tk-number,.nm,.token-num{color:var(--c-num) !important}
.c-fn,.tk-func,.fn,.token-func{color:var(--c-fn) !important}
.c-type,.c-ty,.tk-type,.token-type{color:var(--c-kw) !important}
.c-op,.op,.cmp-op,.tk-ident,.tk-macro,.pp,.tk-punc,.tk-comment{color:var(--code-fg) !important}
.tk-comment,.c-cm{color:var(--c-cmt) !important}

/* 2) Hộp/khung nội dung có nền tối gõ cứng -> nền theo chuẩn (tự đổi). */
.quiz-box,.explain,.q-card,.lab-container,.lab-visual,.grid-board,.grid-vis,
.sim-controls,.score-box,.var-item,.var-box,.var-badge,.info-panel,.set-box,
.map-entry,.hero-insight,.array-cell,.bucket-tube,.reg-item,.quiz,.quiz-opt,
.quiz-exp,.quiz-expl,.pitfall-col,.pitfall-card,.lab-bar,.formula-box,
.mini-interactive,.visual-area,.state-panel,.info-box,.io-table,.styled-table,
.say,.lab-msg,.word-box,.block-label,.col,.pit-col,.cmp-lab,.formula-b,
.bucket-text,.grid-vis,.hero-insight{
  background:var(--card) !important;
}

/* 3) Chữ nội dung gõ cứng màu sáng -> màu chữ chuẩn. */
.qt,.q-text,.math-display,.reg-val,.bucket-text,.quiz-q,.lab-msg,.explain,
.explain *,.quiz-box p,.quiz-box h4,.q-card *,
.say,.say *,.formula-box,.formula-box *,.fv,.word-box,.word-box *,.col,.pit-col,
.lab-msg *,.quiz p,.quiz h4{
  color:var(--fg) !important;
}

/* 4) Ô bảng: tiêu đề dùng màu nhấn, ô thường dùng màu chữ chuẩn. */
.box th, .tablewrap th, table th{color:var(--blue) !important}
.box td, .tablewrap td, table td{color:var(--fg)}
""" + MOC_CUOI


def main():
    ghi = '--ghi' in sys.argv
    tong = 0
    for dp, dn, fn in os.walk(ROOT):
        if '.git' in dp.split(os.sep) or dp.endswith('assets'):
            continue
        for f in sorted(fn):
            if not f.lower().endswith('.html'):
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding='utf-8', errors='replace').read()
            # Trang "theo chuẩn" = có link chuan.css HOẶC nhúng shell nội tuyến
            # (dsu, huffman dùng shell nội tuyến nên nhận biết qua biến --is-dark).
            if 'assets/chuan.css' not in t and '--is-dark' not in t:
                continue
            goc = t
            # gỡ khối cũ nếu chạy lại
            t = re.sub(re.escape(MOC_DAU) + r'.*?' + re.escape(MOC_CUOI), '', t, flags=re.S)
            # chèn vào cuối <style> ĐẦU TIÊN của trang
            m = re.search(r'</style>', t)
            if not m:
                continue
            t = t[:m.start()] + '\n' + KHOI + '\n' + t[m.start():]
            if t != goc:
                tong += 1
                if ghi:
                    open(p, 'w', encoding='utf-8', newline='').write(t)
            r = os.path.relpath(p, ROOT).replace(os.sep, '/')
            print(f'  {"da them" if t != goc else "khong doi":9s} {r}')
    print(('DA GHI' if ghi else 'XEM TRUOC') + f' — {tong} trang')
    return 0


if __name__ == '__main__':
    sys.exit(main())
