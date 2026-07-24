# Kiểm tra quan hệ xâu con

## Mô tả đề bài

Cho hai xâu $s_1$ và $s_2$. Hãy kiểm tra xem một trong hai xâu có phải là xâu con liên tiếp của xâu còn lại hay không và đưa ra kết luận tương ứng:

- Nếu $s_1$ là xâu con liên tiếp của $s_2$, in ra `s1 is substring of s2`, trong đó `s1` và `s2` được thay bằng nội dung thực của hai xâu.
- Ngược lại, nếu $s_2$ là xâu con liên tiếp của $s_1$, in ra `s2 is substring of s1`.
- Nếu không trường hợp nào ở trên xảy ra, in ra `No substring`.

## Dữ liệu

- Dòng thứ nhất chứa xâu $s_1$.
- Dòng thứ hai chứa xâu $s_2$.
- Mỗi xâu có độ dài không vượt quá $30$.

## Kết quả

- In ra kết luận theo quy tắc mô tả ở trên.

## Ví dụ

### Sample input 1
```
ab
cabd
```
### Sample output 1
```
ab is substring of cabd
```

Xâu `ab` xuất hiện liên tiếp bên trong xâu `cabd` nên `ab` là xâu con của `cabd`.
