# Đối xứng của xâu lặp

## Mô tả đề bài

Cho một xâu $s$ gồm các chữ cái la tinh in thường và một số nguyên $k$. Ghép $s$ lặp lại $k$ lần liền nhau để tạo thành một xâu mới $t$. Hãy xác định $t$ có phải là **xâu đối xứng** hay không, tức là đọc từ trái sang phải và đọc từ phải sang trái có giống nhau hay không.

## Dữ liệu

- Dòng thứ nhất: xâu $s$ gồm các chữ cái la tinh in thường ($1 \le |s| \le 250000$).
- Dòng thứ hai: số nguyên $k$ ($1 \le k \le 10^{18}$).

## Kết quả

- Nếu $t$ là xâu đối xứng, ghi ra `YES`; ngược lại ghi ra `NO`.

## Ví dụ

### Sample input 1
```
abc
3
```
### Sample output 1
```
NO
```

### Sample input 2
```
abba
1
```
### Sample output 2
```
YES
```

Trong ví dụ thứ nhất, $t = $ `abcabcabc`, đọc ngược lại thành `cbacbacba` nên không đối xứng. Trong ví dụ thứ hai, $t = $ `abba` vốn đã là xâu đối xứng.
