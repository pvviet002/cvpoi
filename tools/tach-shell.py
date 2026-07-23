# -*- coding: utf-8 -*-
"""Tach nguyen van <style> va <script> cua ChuyenDe/_template/shell.html
thanh assets/chuan.css va assets/chuan.js cua website.
Chep NGUYEN VAN de web va tai lieu chuyen de khong bao gio lech nhau."""
import re, os

SHELL = r"E:\2026-2027\DayThem2026\Contests\ChuyenDe\_template\shell.html"
WEB   = r"E:\2026-2027\DayThem2026\Contests\WEB-LyThuyet\cvpoi"

t = open(SHELL, encoding='utf-8').read()
css = re.search(r'<style>\n(.*?)\n</style>', t, re.S).group(1)
js  = re.search(r'<script>\n(.*?)\n</script>', t, re.S).group(1)

dau_css = """/* =====================================================================
   chuan.css — bộ giao diện chuẩn của chuyên đề.

   TÁCH NGUYÊN VĂN từ ChuyenDe/_template/shell.html (khối <style>).
   KHÔNG sửa tay file này. Muốn đổi thì sửa shell.html rồi chạy lại
   tools/tach-shell.py, để tài liệu chuyên đề và website không bao giờ
   lệch nhau.

   Quy ước dùng: nạp file này TRƯỚC khối <style> riêng của trang, để phần
   CSS của các phòng mô phỏng còn đè lên được.
   ===================================================================== */

"""
dau_js = """/* =====================================================================
   chuan.js — nút đổi nền sáng/tối, tô màu cú pháp C++, nút Sao chép,
   làm nổi mục đang đọc ở thanh bên.

   TÁCH NGUYÊN VĂN từ ChuyenDe/_template/shell.html (khối <script>).
   KHÔNG sửa tay file này — xem chuan.css để biết lý do.
   ===================================================================== */

"""

os.makedirs(os.path.join(WEB, 'assets'), exist_ok=True)
open(os.path.join(WEB, 'assets', 'chuan.css'), 'w', encoding='utf-8', newline='').write(dau_css + css + '\n')
open(os.path.join(WEB, 'assets', 'chuan.js'),  'w', encoding='utf-8', newline='').write(dau_js  + js  + '\n')

print(f'assets/chuan.css : {len(css.splitlines())} dong CSS')
print(f'assets/chuan.js  : {len(js.splitlines())} dong JS')
