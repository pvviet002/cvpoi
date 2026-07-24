# Ký tự lặp liên tiếp

## Mô tả đề bài

Cho một xâu ký tự và một số nguyên $k$. Hãy tìm ký tự **đầu tiên** (tính từ trái sang phải) xuất hiện liên tiếp không ít hơn $k$ lần trong xâu, tức là có một đoạn gồm ít nhất $k$ ký tự giống nhau đứng liền nhau. Nếu không có ký tự nào thoả mãn thì thông báo theo quy định ở phần Kết quả.

## Dữ liệu

- Dòng thứ nhất: số nguyên $k$ ($1 \le k \le 1000$).
- Dòng thứ hai: một xâu chỉ gồm các chữ cái la tinh in hoa và in thường, độ dài không vượt quá $1000$.

## Kết quả

- Một dòng duy nhất: ký tự đầu tiên trong xâu xuất hiện liên tiếp không ít hơn $k$ lần. Nếu không có ký tự nào như vậy, ghi ra `No`.

## Ví dụ

### Sample input 1
```
3
abcccaaab
```
### Sample output 1
```
c
```

Với $k = 3$, ký tự `c` tạo thành đoạn gồm ba ký tự giống nhau đứng liền nhau và là ký tự đầu tiên đạt được điều đó (đoạn ba chữ `a` xuất hiện sau đó).
