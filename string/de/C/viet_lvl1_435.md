# Số đối xứng lớn nhất

## Mô tả đề bài

Một *số đối xứng* (palindrome) là số mà khi đọc từ trái sang phải và từ phải sang trái đều cho cùng một dãy chữ số. Ví dụ, $1221$ và $1234321$ là số đối xứng, còn $1234$ thì không.

Cho $n$ số nguyên dương, hãy tìm số đối xứng lớn nhất trong các số đó. Dữ liệu bảo đảm có ít nhất một số đối xứng.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên dương $n$ ($1 \le n \le 10^4$) — số lượng số.
- $n$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $a_i$ có không quá $32$ chữ số.

## Kết quả

- In ra số đối xứng lớn nhất trong $n$ số đã cho.

## Ví dụ

### Sample input 1
```
5
12321
456
1221
9
1000021
```
### Sample output 1
```
12321
```

Trong các số đã cho, những số đối xứng gồm $12321$, $1221$ và $9$; số lớn nhất trong chúng là $12321$.
