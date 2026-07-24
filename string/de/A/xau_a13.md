# Tìm lần xuất hiện đầu tiên

## Mô tả đề bài

Cho một xâu $S$ và một xâu mẫu $T$. Hãy tìm vị trí xuất hiện đầu tiên của $T$ trong $S$ (vị trí là chỉ số ký tự bắt đầu của lần xuất hiện, đánh số từ $1$). Nếu $T$ không xuất hiện trong $S$, hãy in $-1$.

## Dữ liệu

- Dòng đầu tiên chứa xâu $S$ ($1 \le |S| \le 10^5$), không chứa dấu cách.
- Dòng thứ hai chứa xâu mẫu $T$ ($1 \le |T| \le |S|$), không chứa dấu cách.

## Kết quả

- Một số nguyên là vị trí xuất hiện đầu tiên của $T$, hoặc $-1$ nếu không có.

## Ví dụ

### Sample input 1
```
abcabc
bc
```
### Sample output 1
```
2
```

Lần xuất hiện đầu tiên của `bc` bắt đầu tại vị trí $2$.
