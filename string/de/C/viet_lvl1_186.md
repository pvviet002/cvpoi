# Kiểm tra xâu đối xứng

## Mô tả đề bài

Một xâu được gọi là *đối xứng* (palindrome) nếu khi đọc từ trái sang phải và từ phải sang trái đều cho kết quả giống nhau. Ví dụ, `level` và `abcba` là các xâu đối xứng, còn `hello` thì không.

Cho một xâu, hãy kiểm tra xem nó có phải là xâu đối xứng hay không.

## Dữ liệu

- Một dòng duy nhất chứa xâu cần kiểm tra, độ dài nhỏ hơn $100$.

## Kết quả

- In ra `yes` nếu xâu là đối xứng, ngược lại in ra `no`.

## Ví dụ

### Sample input 1
```
level
```
### Sample output 1
```
yes
```

### Sample input 2
```
hello
```
### Sample output 2
```
no
```

Xâu `level` đọc xuôi và đọc ngược đều cho `level` nên là xâu đối xứng; xâu `hello` đọc ngược là `olleh` nên không phải xâu đối xứng.
