# Nén xâu số

## Mô tả đề bài

Cho một xâu chỉ gồm các chữ số từ `0` đến `9`. Ta nén xâu này bằng cách xét lần lượt từng cụm các chữ số **giống nhau đứng liền nhau**: với mỗi cụm, ghi ra số lượng chữ số của cụm rồi ghi chính chữ số đó.

Chẳng hạn xâu `122344111` gồm các cụm `1`, `22`, `3`, `44`, `111`, nên kết quả nén là `11 22 13 24 31` viết liền thành `1122132431`.

Hãy đưa ra xâu nén của xâu đã cho.

## Dữ liệu

- Một dòng duy nhất chứa xâu gồm các chữ số `0`–`9`, độ dài không vượt quá $1000$.

## Kết quả

- Một dòng duy nhất là xâu nén thu được.

## Ví dụ

### Sample input 1
```
122344111
```
### Sample output 1
```
1122132431
```

### Sample input 2
```
00000000000
```
### Sample output 2
```
110
```

Ở ví dụ thứ hai, cả xâu là một cụm gồm $11$ chữ số `0`, nên kết quả là số lượng $11$ ghép với chữ số `0`.
