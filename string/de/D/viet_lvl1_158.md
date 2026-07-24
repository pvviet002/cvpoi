# Ký tự xuất hiện đúng một lần

## Mô tả đề bài

Cho một xâu chỉ gồm các chữ cái la tinh in thường. Hãy tìm ký tự **đầu tiên** (tính từ trái sang phải) chỉ xuất hiện đúng một lần trong xâu. Nếu không tồn tại ký tự nào như vậy thì thông báo theo quy định ở phần Kết quả.

## Dữ liệu

- Một dòng duy nhất chứa xâu gồm các chữ cái la tinh in thường, độ dài nhỏ hơn $1100$.

## Kết quả

- Một dòng duy nhất: ký tự đầu tiên chỉ xuất hiện đúng một lần trong xâu. Nếu không có ký tự nào như vậy, ghi ra `no`.

## Ví dụ

### Sample input 1
```
abcabd
```
### Sample output 1
```
c
```

### Sample input 2
```
aabbcc
```
### Sample output 2
```
no
```

Trong ví dụ thứ nhất, hai ký tự `a` và `b` đều xuất hiện hai lần, còn `c` và `d` mỗi ký tự xuất hiện một lần; `c` đứng trước `d`. Trong ví dụ thứ hai, mọi ký tự đều xuất hiện hai lần nên đáp án là `no`.
