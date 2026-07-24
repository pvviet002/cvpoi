# Đếm đoạn gen khác nhau

## Mô tả đề bài

Một bộ gen được biểu diễn bằng một xâu chỉ gồm bốn chữ cái `A`, `T`, `C`, `G`. Nhiều đoạn trong bộ gen lặp lại nhiều lần, và người ta muốn thống kê mức độ lặp đó.

Một đoạn con liên tiếp có độ dài $k$ của bộ gen được gọi là một *$k$-đoạn*. Hãy đếm số $k$-đoạn **khác nhau** xuất hiện trong bộ gen. Ví dụ, bộ gen `TACAC` có các $2$-đoạn là `TA`, `AC`, `CA`, `AC`, trong đó số đoạn khác nhau là $3$.

Bộ gen không cho trực tiếp mà được sinh ra từ dãy số $R$ như sau: số nguyên $R_1$ được cho trong dữ liệu ($0 \le R_1 < 201701$). Với $i > 1$:

$$R_i = (R_{i-1} \times 6807 + 2831) \bmod 201701.$$

Ký tự thứ $i$ của bộ gen ($1 \le i \le n$) được xác định theo giá trị $R_i \bmod 4$: các giá trị $0$, $1$, $2$, $3$ tương ứng với `A`, `T`, `C`, `G`.

## Dữ liệu

- Một dòng chứa ba số nguyên $n$, $k$, $R_1$ — độ dài bộ gen, độ dài của đoạn và số hạng đầu của dãy sinh, với $1 \le n \le 10^5$, $1 \le k \le 10$, $0 \le R_1 < 201701$.

## Kết quả

- Một dòng duy nhất chứa một số nguyên là số $k$-đoạn khác nhau trong bộ gen.

## Ví dụ

### Sample input 1
```
20 2 37
```
### Sample output 1
```
10
```

Với dữ liệu này, bộ gen sinh ra là `TTCGATAGGTCAGTTATCAG` (dài $20$), và trong đó có tất cả $10$ đoạn độ dài $2$ khác nhau.
