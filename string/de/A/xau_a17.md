# So sánh hai xâu

## Mô tả đề bài

Cho hai xâu ký tự. Hãy so sánh chúng theo thứ tự từ điển và cho biết quan hệ giữa xâu thứ nhất và xâu thứ hai: in dấu `<` nếu xâu thứ nhất đứng trước, dấu `>` nếu xâu thứ nhất đứng sau, hoặc dấu `=` nếu hai xâu giống hệt nhau.

## Dữ liệu

- Dòng đầu tiên chứa xâu thứ nhất.
- Dòng thứ hai chứa xâu thứ hai.
- Hai xâu không chứa dấu cách, mỗi xâu có độ dài không vượt quá $10^5$.

## Kết quả

- Một dòng chứa một trong ba ký tự `<`, `>` hoặc `=`.

## Ví dụ

### Sample input 1
```
apple
apply
```
### Sample output 1
```
<
```

Hai xâu giống nhau đến vị trí thứ $4$; tại vị trí thứ $5$, `e` đứng trước `y` nên xâu `apple` đứng trước.
