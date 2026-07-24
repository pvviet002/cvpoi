# Thay đoạn con

## Mô tả đề bài

Cho một xâu $S$, một vị trí $p$, một độ dài $L$ và một xâu $R$. Hãy thay $L$ ký tự liên tiếp bắt đầu từ vị trí $p$ của $S$ (các vị trí đánh số từ $1$) bằng xâu $R$, rồi in ra xâu thu được. Xâu $R$ không nhất thiết có cùng độ dài với đoạn bị thay.

## Dữ liệu

- Dòng đầu tiên chứa xâu $S$ ($1 \le |S| \le 10^5$), không chứa dấu cách.
- Dòng thứ hai chứa hai số nguyên $p$ và $L$ ($1 \le p \le |S|$, $0 \le L$, $p + L - 1 \le |S|$).
- Dòng thứ ba chứa xâu $R$, không chứa dấu cách.

## Kết quả

- Một dòng duy nhất là xâu sau khi thay.

## Ví dụ

### Sample input 1
```
abcdef
2 3
XYZW
```
### Sample output 1
```
aXYZWef
```

Ba ký tự `bcd` được thay bằng xâu `XYZW`.
