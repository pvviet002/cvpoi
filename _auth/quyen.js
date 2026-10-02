/* Luật xem trang — sửa tay rồi git push. Phần sau "export default" phải là
   JSON thuần (không chú thích, không dấu phẩy thừa) vì tools/tai-khoan.py
   cũng đọc tệp này.

   Mỗi luật: {"duong": "/thư-mục/", "nhom": [...]}
     "nhom": ["mo"]            ai cũng xem được, không cần đăng nhập
     "nhom": ["*"]             có tài khoản là xem được
     "nhom": ["hsg9","hsg12"]  chỉ tài khoản thuộc một trong các nhóm này
   Nhóm "giaovien" luôn xem được mọi trang.

   Trang không khớp luật nào thì MỞ (lý thuyết công khai). Một trang khớp
   nhiều luật thì luật có "duong" dài nhất thắng; luật có "chinhxac": true
   chỉ áp cho đúng đường dẫn đó và thắng mọi luật khác.

   Thêm thư mục lời giải mới thì thêm một dòng ở đây, rồi soát bằng
     python tools/tai-khoan.py quyen */
export default [
  {"duong": "/sols/", "chinhxac": true, "nhom": ["mo"]},
  {"duong": "/sols/", "nhom": ["*"]},
  {"duong": "/sols/2627_hsg12_", "nhom": ["hsg12"]},
  {"duong": "/sols/2526hsg9-thithu-c1/", "nhom": ["hsg9"]},
  {"duong": "/sols/hsg9-2627-21/", "nhom": ["hsg9"]},
  {"duong": "/hsg9/", "nhom": ["hsg9"]},
  {"duong": "/hsg9/hsg9_2627_33/", "nhom": ["mo"]},

  {"duong": "/array-1d/sols/", "nhom": ["*"]},
  {"duong": "/array-2d/arr2d_", "nhom": ["*"]},
  {"duong": "/prefix-sum/1d/differentarray_09/", "nhom": ["*"]},
  {"duong": "/prefix-sum/1d/prefixsum_05/", "nhom": ["*"]},
  {"duong": "/prefix-sum/1d/prefixsum_optimize/", "nhom": ["*"]},
  {"duong": "/prefix-sum/2d/", "nhom": ["*"]},
  {"duong": "/tree/sols/", "nhom": ["*"]},
  {"duong": "/tree/viet_lvl", "nhom": ["*"]},
  {"duong": "/dp/range/", "nhom": ["*"]},
  {"duong": "/graph-basic/sodokhoi/", "nhom": ["*"]},
  {"duong": "/inclusion-exclusion/includion-exclusion-01/", "nhom": ["*"]}
];
