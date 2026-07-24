# Tổng các số trên mỗi dòng

## Mô tả đề bài

Cho một số dòng văn bản. Mỗi dòng chứa một số số nguyên, xen giữa chúng có thể là các ký tự khác. Với mỗi dòng, hãy tính tổng của tất cả các số nguyên xuất hiện trên dòng đó. Nếu một dòng không chứa số nào thì không in ra gì cho dòng đó.

Quy ước về cách nhận biết số:

- Một số nguyên là một dãy các chữ số liền nhau; số có thể mang dấu âm nếu ngay trước dãy chữ số có một dấu `-` đóng vai trò dấu âm.
- Ký tự `.` luôn được coi là ký tự ngăn cách, không bao giờ là một phần của số.
- Giữa hai số nguyên bất kỳ luôn có ít nhất một ký tự ngăn cách. Do đó, nếu chỉ có đúng một dấu `-` nằm kẹp trực tiếp giữa hai dãy chữ số thì dấu `-` đó là ký tự ngăn cách chứ không phải dấu âm.

## Dữ liệu

- Gồm không quá $100$ dòng, đọc đến hết tệp. Mỗi dòng là một xâu ký tự dài không quá $1000$ ký tự và chứa không quá $200$ số nguyên. Mỗi số nguyên có giá trị trong đoạn $[-10^7, 10^7]$.

## Kết quả

- Với mỗi dòng có chứa ít nhất một số nguyên, in ra một dòng chứa tổng các số nguyên trên dòng đó (giữ đúng thứ tự các dòng của dữ liệu).

## Ví dụ

### Sample input 1
```
su57jdkjth54hjsns-321d 8 ejre
erg(&-^%

weruy4uhnd-
```
### Sample output 1
```
-202
4
```

Dòng $1$ chứa các số $57$, $54$, $-321$, $8$ nên tổng là $-202$. Dòng $2$ và dòng $3$ không có số nào nên bị bỏ qua. Dòng $4$ chỉ có một số là $4$.

### Sample input 2
```
1-1
1 -1
1--5
1-----------1
-1-1
--1
-2.3
```
### Sample output 2
```
2
0
-4
0
0
-1
1
```

Ở dòng `1-1`, dấu `-` là ký tự ngăn cách giữa hai số $1$ nên tổng là $2$. Ở dòng `-1-1`, số đầu là $-1$ nên dấu `-` thứ hai đóng vai trò ngăn cách, cho tổng $-1 + 1 = 0$. Ở dòng `-2.3`, dấu `.` là ngăn cách nên có hai số $-2$ và $3$, tổng bằng $1$.
