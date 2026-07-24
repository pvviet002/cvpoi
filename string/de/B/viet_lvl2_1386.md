# Mã sản phẩm

## Mô tả đề bài

Một cửa hàng cần chuẩn hoá lại toàn bộ mã sản phẩm của mình.

Mã cũ là một xâu gồm các chữ cái Latin in hoa, các chữ cái Latin in thường và các số nguyên (có thể dương hoặc âm). Chẳng hạn mã `cG23mH-9s` chứa hai chữ in hoa, ba chữ in thường, một số nguyên dương và một số nguyên âm.

Mã mới được tạo ra từ mã cũ theo quy tắc: xoá toàn bộ chữ in thường, giữ lại tất cả chữ in hoa theo đúng thứ tự cũ, rồi ghi tổng của tất cả các số nguyên trong mã cũ vào cuối. Chẳng hạn mã mới của `cG23mH-9s` là `GH14`, vì tổng các số nguyên là $23 + (-9) = 14$.

Hãy sinh mã mới cho tất cả các mã cũ được cho.

## Dữ liệu

- Dòng đầu tiên: một số nguyên dương $N$ ($1 \le N \le 1000$) — số lượng mã cần chuẩn hoá.
- $N$ dòng tiếp theo: mỗi dòng chứa một mã cũ. Mã chỉ gồm chữ cái Latin, chữ số và dấu `-`; tổng độ dài các mã không vượt quá $10^6$.
- Mỗi mã chứa ít nhất một chữ in hoa, một chữ in thường và một số nguyên. Mỗi số nguyên có không quá $9$ chữ số.
- Dấu `-` luôn là dấu của một số nguyên âm và luôn đứng ngay trước chữ số đầu tiên của số đó.
- Một số nguyên dương không bao giờ đứng ngay sau một số nguyên khác. Nghĩa là cụm `23` luôn được hiểu là số $23$, chứ không phải hai số $2$ và $3$.

## Kết quả

- Ghi ra $N$ dòng, dòng thứ $i$ là mã mới của mã cũ thứ $i$.

## Ví dụ

### Sample input 1
```
1
AbC3c2Cd9
```
### Sample output 1
```
ACC14
```

Ba chữ in hoa `A`, `C`, `C`; ba số nguyên $3$, $2$, $9$.

### Sample input 2
```
3
Ahkiy-6ebvXCV1
393hhhUHkbs5gh6QpS-9-8
PL12N-2G1234Duytrty8-86tyaYySsDdEe
```
### Sample output 2
```
AXCV-5
UHQS387
PLNGDYSDE1166
```

Cụm `393` là một số nguyên, không phải ba số $3$, $9$, $3$. Cụm `-9-8` là hai số nguyên âm đứng liền nhau.

## Ràng buộc

| Subtask | Điểm | Ràng buộc bổ sung |
| ------- | ---- | ----------------- |
| 1 | 30% | Mọi số nguyên trong các mã đều dương và có đúng một chữ số |
| 2 | 30% | Mọi số nguyên trong các mã đều có đúng một chữ số |
| 3 | 40% | Không có thêm ràng buộc bổ sung |
