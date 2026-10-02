/* Danh sách tài khoản — do tools/tai-khoan.py sinh, ĐỪNG sửa tay.
   Mật khẩu chỉ lưu dạng băm (PBKDF2-SHA256 kèm muối), không khôi phục lại được.
   Thêm / xoá / đổi nhóm / đặt lại mật khẩu: python tools/tai-khoan.py --help */
export default {
 "viet": {
  "ten": "Phan Văn Việt",
  "nhom": [
   "giaovien"
  ],
  "muoi": "fc8b6d9bcd5075505a59c5d245914492",
  "vong": 100000,
  "bam": "ef68db538ecde688b71bec934ee9da0fed3c330087562a5d1131f64ae5a52a56"
 }
};
