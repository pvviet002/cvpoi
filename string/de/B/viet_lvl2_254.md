# Hiệu hai số lớn

## Mô tả đề bài

Cho hai số nguyên dương $a$ và $b$. Hãy tính giá trị $a - b$. Kết quả có thể là số âm; khi đó cần in kèm dấu trừ ở đầu.

Hai số có thể có rất nhiều chữ số, vượt xa sức chứa của mọi kiểu số nguyên dựng sẵn, nên cần biểu diễn và trừ chúng dưới dạng xâu chữ số.

## Dữ liệu

- Dòng đầu tiên chứa số $a$.
- Dòng thứ hai chứa số $b$.
- Mỗi số không chứa dấu ($0 < a, b \le 10^{10086}$).

## Kết quả

- Một dòng duy nhất chứa giá trị $a - b$. Nếu $a - b < 0$ thì in kèm dấu trừ ở đầu.

## Ví dụ

### Sample input 1
```
2
1
```
### Sample output 1
```
1
```

Ta có $2 - 1 = 1$.

### Sample input 2
```
1
100
```
### Sample output 2
```
-99
```

Ta có $1 - 100 = -99$; kết quả âm nên có dấu trừ ở đầu.
