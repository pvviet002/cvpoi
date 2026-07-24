# Xoá đoạn con

## Mô tả đề bài

Cho một xâu $S$, một vị trí $p$ và một độ dài $L$. Hãy xoá khỏi xâu $L$ ký tự liên tiếp bắt đầu từ vị trí $p$ (các vị trí đánh số từ $1$), rồi in ra xâu còn lại.

## Dữ liệu

- Dòng đầu tiên chứa xâu $S$ ($1 \le |S| \le 10^5$), không chứa dấu cách.
- Dòng thứ hai chứa hai số nguyên $p$ và $L$ ($1 \le p \le |S|$, $0 \le L$, $p + L - 1 \le |S|$).

## Kết quả

- Một dòng duy nhất là xâu sau khi xoá.

## Ví dụ

### Sample input 1
```
abcdefg
3 2
```
### Sample output 1
```
abefg
```

Hai ký tự `c`, `d` (ở vị trí $3$ và $4$) đã bị xoá.
