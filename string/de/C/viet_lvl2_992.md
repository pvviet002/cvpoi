# Đếm số lần xuất hiện của xâu con

## Mô tả đề bài

Cho $T$ truy vấn. Mỗi truy vấn cho hai xâu $a$ và $b$ có độ dài lần lượt là $n$ và $m$, chỉ gồm các chữ cái tiếng Anh. Hãy đếm số lần xâu $a$ xuất hiện như một xâu con liên tiếp trong xâu $b$. Khi so khớp, không phân biệt chữ hoa và chữ thường.

## Dữ liệu

- Dòng đầu tiên chứa một số nguyên dương $T$ ($T \le 100$) — số truy vấn.
- Tiếp theo là $T$ nhóm, mỗi nhóm gồm $3$ dòng:
  - Dòng thứ nhất chứa hai số nguyên dương $n$ và $m$.
  - Dòng thứ hai chứa xâu $a$ có độ dài $n$.
  - Dòng thứ ba chứa xâu $b$ có độ dài $m$.
- Tổng các giá trị $n$ và tổng các giá trị $m$ đều không vượt quá $10^3$ ($\sum n \le \sum m \le 10^3$).

## Kết quả

- In ra $T$ dòng, dòng thứ $i$ là một số nguyên — đáp án của truy vấn thứ $i$.

## Ví dụ

### Sample input 1
```
5
3 10
abc
abcabcabca
2 10
aa
AAaAaaAaAa
5 5
AbCdE
eDcBa
5 5
abcde
ABCDE
3 10
aba
ABaBaAbaBA
```
### Sample output 1
```
3
9
0
1
4
```

Ở truy vấn thứ nhất, `abc` xuất hiện $3$ lần trong `abcabcabca`. Ở truy vấn thứ hai, do không phân biệt hoa thường nên `aa` khớp tại $9$ vị trí. Ở truy vấn thứ tư, `abcde` khớp `ABCDE` đúng một lần.
