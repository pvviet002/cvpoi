# -*- coding: utf-8 -*-
"""
len-chuan.py — đưa một trang bài học về đúng bộ giao diện chuẩn
(ChuyenDe/_template/shell.html), nhưng GIỮ NGUYÊN các phòng mô phỏng.

    python tools/len-chuan.py <đường-dẫn-trang>        # xem trước
    python tools/len-chuan.py <đường-dẫn-trang> --ghi  # ghi thật
    python tools/len-chuan.py --tat-ca --ghi           # làm mọi trang đã khai

Việc công cụ làm:
  1. Bỏ mọi liên kết font ngoài / CDN, nạp assets/chuan.css.
  2. Trong khối <style> riêng của trang:
     - thay khối :root bằng bảng ÁNH XẠ biến cũ sang biến của chuẩn, nhờ đó
       toàn bộ CSS của phòng mô phỏng tự đổi màu theo nền sáng/tối mà không
       phải viết lại;
     - xoá các quy tắc ở mức tài liệu (body, h1..h4, p, ul, .container...) vì
       chuan.css đã lo;
     - thu hẹp quy tắc `button {}` trần vào trong phòng mô phỏng, để không đè
       nút đổi nền và nút Sao chép của chuẩn.
  3. Thêm nút đổi nền, thanh bên mục lục, bọc nội dung trong .main > .wrap.
  4. Nạp assets/chuan.js ở cuối trang.

Phần thân trang khác nhau quá nhiều giữa các trang nên mỗi trang có một mục
khai báo riêng trong TRANG bên dưới.
"""

import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================================================
#  Ánh xạ biến màu: tên biến cũ  ->  biểu thức theo biến của chuẩn.
#  Tên nào TRÙNG với biến của chuẩn (--bg, --red, --green, --amber,
#  --purple, --blue) thì bỏ hẳn, để định nghĩa của chuẩn có hiệu lực.
# =====================================================================
ANH_XA_TOI = {                      # họ trang nền xanh đậm của website
    '--bg2':        'var(--card)',
    '--panel':      'var(--card)',
    '--panel2':     'var(--card)',
    '--line':       'var(--border)',
    '--line2':      'var(--border)',
    '--rule':       'var(--border)',
    '--border':     'var(--border)',
    '--ink':        'var(--fg)',
    '--ink-soft':   'var(--muted)',
    '--ink-dim':    'var(--muted)',
    '--text-main':  'var(--fg)',
    '--text-muted': 'var(--muted)',
    '--accent':     'var(--green)',
    '--accent-dim': 'var(--green-bg)',
    '--accent2':    'var(--blue)',
    '--accent-blue':'var(--blue)',
    '--mark':       'var(--amber)',
    '--highlight':  'var(--amber)',
    '--pink':       'var(--purple)',
    '--lca':        'var(--purple)',
    '--jump':       'var(--purple)',
    '--correct':    'var(--green)',
    '--wrong':      'var(--red)',
    '--shadow':     'none',
    '--shadow-card':'none',
    '--glow':       'none',
    '--glow-a':     'none',
    '--glow-m':     'none',
    '--glow-j':     'none',
    '--glow-l':     'none',
    '--font-body':  '"Noto Sans","Segoe UI",system-ui,sans-serif',
    '--font-head':  '"Noto Sans","Segoe UI",system-ui,sans-serif',
    '--font-heading':'"Noto Sans","Segoe UI",system-ui,sans-serif',
    '--font-mono':  '"Noto Sans Mono","Consolas",ui-monospace,monospace',
    '--font-code':  '"Noto Sans Mono","Consolas",ui-monospace,monospace',
}

# Quy tắc ở mức tài liệu — chuan.css đã lo, xoá đi kẻo đánh nhau.
BO_CHON_XOA = (r'\*|html|body|body::before|body::after|section|h1|h2|h3|h4|'
               r'p|ul|ol|li|a|strong|em|footer|nav|'
               r'\.container|\.wrap|\.content|\.breadcrumb|\.nav-inner|\.nav-links|'
               r'\.nav-btn|\.nav-sticky|\.sticky-nav|\.home-btn|\.crumb|\.eyebrow|'
               r'\.hero-top|\.hero-meta|\.hero-sub|\.lead|\.kicker')

MAU_CUNG = [                       # màu gõ cứng còn sót -> biến của chuẩn
    (r'#0A1220\b', 'var(--code-bg)'), (r'#0a1220\b', 'var(--code-bg)'),
    (r'#A9B7C6\b', 'var(--code-fg)'), (r'#a9b7c6\b', 'var(--code-fg)'),
]


def go_the(text, tag, giu_lai=None):
    """Xoá mọi thẻ <tag ...>...</tag>; giu_lai(khoi) trả True thì chừa lại."""
    ra, vt = [], 0
    while True:
        m = re.search(r'<' + tag + r'\b[^>]*>', text[vt:], re.I)
        if not m:
            ra.append(text[vt:]); break
        dau = vt + m.start()
        dong = re.search(r'</' + tag + r'\s*>', text[dau:], re.I)
        if not dong:
            ra.append(text[vt:]); break
        het = dau + dong.end()
        khoi = text[dau:het]
        if giu_lai and giu_lai(khoi):
            ra.append(text[vt:het])
        else:
            ra.append(text[vt:dau])
        vt = het
    return ''.join(ra)


def xoa_quy_tac(css, bo_chon):
    """Xoá các quy tắc CSS có bộ chọn khớp bo_chon (chỉ ở cấp ngoài cùng).

    Phải bỏ chú thích đứng trước bộ chọn rồi mới so khớp: nếu không thì
    `/* Typography */\\n h1 {...}` sẽ lọt lưới vì `^\\s*` không nuốt được
    chú thích — đã vấp đúng lỗi này."""
    ra, i, n = [], 0, len(css)
    mau = re.compile(r'^\s*(' + bo_chon + r')(\s*,\s*(' + bo_chon + r'))*\s*\{')
    while i < n:
        j = css.find('{', i)
        if j < 0:
            ra.append(css[i:]); break
        dau_dong = css.rfind('\n', 0, i) + 1
        bo = css[i:j + 1]
        # bỏ qua @media / @keyframes: giữ nguyên cả khối
        if bo.lstrip().startswith('@'):
            muc, k = 1, j + 1
            while k < n and muc:
                if css[k] == '{': muc += 1
                elif css[k] == '}': muc -= 1
                k += 1
            ra.append(css[i:k]); i = k; continue
        k = css.find('}', j)
        if k < 0:
            ra.append(css[i:]); break
        k += 1
        bo_sach = re.sub(r'/\*.*?\*/', '', bo, flags=re.S)   # bỏ chú thích rồi mới khớp
        if mau.match(bo_sach):
            pass                      # bỏ quy tắc này
        else:
            ra.append(css[i:k])
        i = k
    return re.sub(r'\n{3,}', '\n\n', ''.join(ra))


def sua_css(css, khung_nut='.lab'):
    # 1. :root -> bảng ánh xạ
    def thay_root(m):
        cu = dict(re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', m.group(1)))
        dong = ['        /* Ánh xạ biến cũ của trang sang biến của chuẩn, nhờ đó phần',
                '           CSS phòng mô phỏng bên dưới tự theo nền sáng/tối. */',
                ':root{']
        for ten in cu:
            if ten in ANH_XA_TOI:
                dong.append(f'  {ten}: {ANH_XA_TOI[ten]};')
        dong.append('}')
        return '\n'.join(dong)
    css = re.sub(r':root\s*\{(.*?)\}', thay_root, css, count=1, flags=re.S)
    # 2. xoá quy tắc mức tài liệu
    css = xoa_quy_tac(css, BO_CHON_XOA)
    # 3. Thu hẹp quy tắc `button` trần vào trong các khung mô phỏng.
    #    Phải nhân bộ chọn cho TỪNG khung: viết ".a, .b button" thì ".a" và ".b"
    #    tự nhận luôn kiểu của nút — đã vấp, làm hỏng cả khung mô phỏng.
    #    Phải nhân cả phần đuôi bộ chọn (:hover, :disabled, .primary…) cho từng
    #    khung, nếu không thì đuôi chỉ dính vào bộ chọn cuối cùng.
    khung = [x.strip() for x in khung_nut.split(',') if x.strip()]
    def nhan_ban(m):
        duoi = m.group(2)
        return m.group(1) + ', '.join(f'{k} button{duoi}' for k in khung) + '{'
    css = re.sub(r'^([ \t]*)button\b([^{,\n]*)\{', nhan_ban, css, flags=re.M)
    # 4. màu gõ cứng
    for cu, moi in MAU_CUNG:
        css = re.sub(cu, moi, css)
    return css


def thanh_ben(ten, muc):
    d = '\n'.join(f'  <a href="#{i}">{n}. {nh}</a>' for n, (i, nh) in enumerate(muc, 1))
    return f'<aside class="side">\n  <div class="hd">{ten}</div>\n{d}\n</aside>'


def muc_luc(muc):
    d = '\n'.join(f'    <li><a href="#{i}">{nh}</a></li>' for i, nh in muc)
    return f'<nav class="toc">\n  <b>Nội dung</b>\n  <ol>\n{d}\n  </ol>\n</nav>'


def dau_trang(ten, phu=''):
    p = f'\n\n<p>{phu}</p>' if phu else ''
    return (f'<header>\n  <div class="kicker">Chuyên đề Lập trình thi đấu</div>\n'
            f'  <h1>{ten}</h1>\n'
            f'  <div class="by">Phan Văn Việt — Trường THPT Chuyên Vĩnh Phúc</div>\n</header>{p}')
