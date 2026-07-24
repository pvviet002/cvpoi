# Bình chọn số phiếu cao nhất

## Mô tả đề bài

Có $n$ ứng viên tham gia một cuộc bình chọn. Số phiếu của mỗi ứng viên là một số nguyên có thể rất lớn, lên tới $100$ chữ số. Hãy xác định ứng viên có số phiếu cao nhất, rồi đưa ra số thứ tự và số phiếu của người đó. Bảo đảm không có hai ứng viên nào có cùng số phiếu.

## Dữ liệu

- Dòng đầu tiên chứa một số nguyên $n$ ($1 \le n \le 20$) — số ứng viên.
- $n$ dòng tiếp theo, dòng thứ $i$ chứa số phiếu của ứng viên thứ $i$, là một số nguyên có tới $100$ chữ số.

## Kết quả

- Dòng đầu tiên chứa số thứ tự của ứng viên có số phiếu cao nhất.
- Dòng thứ hai chứa số phiếu của ứng viên đó.

## Ví dụ

### Sample input 1
```
5
98765
12365
87954
1022356
985678
```
### Sample output 1
```
4
1022356
```

Ứng viên thứ $4$ có $1022356$ phiếu, nhiều hơn số phiếu của mọi ứng viên còn lại.
