# Trích xâu con

## Mô tả đề bài

Cho một xâu $S$, một vị trí $p$ và một độ dài $L$. Hãy in ra xâu con gồm $L$ ký tự liên tiếp bắt đầu từ vị trí $p$ của $S$ (các vị trí đánh số từ $1$).

## Dữ liệu

- Dòng đầu tiên chứa xâu $S$ ($1 \le |S| \le 10^5$), không chứa dấu cách.
- Dòng thứ hai chứa hai số nguyên $p$ và $L$ ($1 \le p \le |S|$, $0 \le L$, $p + L - 1 \le |S|$).

## Kết quả

- Một dòng duy nhất là xâu con thu được.

## Ví dụ

### Sample input 1
```
programming
4 5
```
### Sample output 1
```
gramm
```

Năm ký tự bắt đầu từ vị trí $4$ của `programming` tạo thành xâu con `gramm`.
