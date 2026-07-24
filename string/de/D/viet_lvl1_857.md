# Kiểm tra số lần xuất hiện chẵn

## Mô tả đề bài

Cho một xâu gồm các chữ cái la tinh in thường. Hãy kiểm tra xem **mỗi loại ký tự** trong xâu có xuất hiện một số lần chẵn hay không, rồi thông báo kết quả theo quy định ở phần Kết quả.

## Dữ liệu

- Một dòng duy nhất chứa một xâu gồm các chữ cái la tinh in thường, độ dài từ $1$ đến $10^6$.

## Kết quả

- Nếu mỗi loại ký tự trong xâu đều xuất hiện một số lần chẵn, ghi ra `YES`; ngược lại ghi ra `NO`.

## Ví dụ

### Sample input 1
```
banana
```
### Sample output 1
```
NO
```

### Sample input 2
```
bbnana
```
### Sample output 2
```
YES
```

Trong ví dụ thứ nhất, ký tự `a` xuất hiện $3$ lần (số lẻ) nên kết quả là `NO`. Trong ví dụ thứ hai, ba loại ký tự `b`, `n`, `a` mỗi loại xuất hiện đúng $2$ lần nên kết quả là `YES`.
