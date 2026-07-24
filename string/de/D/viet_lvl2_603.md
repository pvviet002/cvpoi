# Từ xuất hiện nhiều nhất

## Mô tả đề bài

Trong xử lý văn bản, việc thống kê tần suất xuất hiện của các từ là một công việc thường gặp. Cho $n$ từ, hãy tìm từ xuất hiện nhiều lần nhất. Khi so sánh, **bỏ qua sự phân biệt chữ hoa và chữ thường** (nghĩa là `Apple`, `apple`, `APPLE`, `aPPle` đều được coi là cùng một từ). Dữ liệu bảo đảm chỉ có duy nhất một từ đạt số lần xuất hiện nhiều nhất.

## Dữ liệu

- Dòng thứ nhất: số nguyên $n$ ($1 \le n \le 100$) — số lượng từ.
- $n$ dòng tiếp theo, mỗi dòng chứa một từ gồm các chữ cái la tinh in hoa hoặc in thường, độ dài không vượt quá $30$.

## Kết quả

- Một dòng duy nhất chứa từ xuất hiện nhiều lần nhất, viết dưới dạng **chữ thường**.

## Ví dụ

### Sample input 1
```
6
Apple
banana
apple
Orange
banana
apple
```
### Sample output 1
```
apple
```

Sau khi bỏ phân biệt hoa thường, từ `apple` xuất hiện $3$ lần (từ `Apple` và hai từ `apple`), nhiều hơn `banana` ($2$ lần) và `orange` ($1$ lần).
