# Chèn xâu

## Mô tả đề bài

Cho hai xâu $A$, $B$ và một vị trí $k$. Hãy chèn toàn bộ xâu $B$ vào xâu $A$ ngay trước ký tự thứ $k$ của $A$ (các vị trí đánh số từ $1$). Nếu $k = |A| + 1$ thì $B$ được nối vào cuối $A$. Hãy in ra xâu thu được.

## Dữ liệu

- Dòng đầu tiên chứa xâu $A$.
- Dòng thứ hai chứa xâu $B$.
- Dòng thứ ba chứa số nguyên $k$ ($1 \le k \le |A| + 1$).
- Hai xâu không chứa dấu cách, tổng độ dài không vượt quá $10^5$.

## Kết quả

- Một dòng duy nhất là xâu sau khi chèn.

## Ví dụ

### Sample input 1
```
abcd
XY
3
```
### Sample output 1
```
abXYcd
```

Xâu `XY` được đặt ngay trước ký tự thứ $3$ (chữ `c`) của `abcd`.
