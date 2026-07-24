# Hai xâu tương tự

## Mô tả đề bài

Với hai xâu $A$ và $B$, nếu $A$ có thể biến thành $B$ bằng cách **xoá một ký tự**, **hoặc chèn thêm một ký tự**, **hoặc thay đổi một ký tự**, thì ta nói $A$ và $B$ là *tương tự*.

Ví dụ, `apple` có thể chèn thêm một ký tự để thành `applee`, có thể xoá một ký tự để thành `appe`, cũng có thể đổi một ký tự để thành `bpple`; do đó `apple` tương tự với `applee`, `appe` và `bpple`. Tuy nhiên, `applee` không thể chỉ qua một thao tác mà biến thành `bpple`, nên chúng không tương tự. Đặc biệt, hai xâu hoàn toàn giống nhau cũng được coi là tương tự.

Cho $T$ cặp xâu $A$ và $B$, hãy xác định với mỗi cặp chúng có tương tự hay không.

## Dữ liệu

- Dòng thứ nhất: số nguyên dương $T$ ($1 \le T \le 100$) — số cặp xâu.
- $T$ dòng tiếp theo, mỗi dòng chứa hai xâu $A$ và $B$ cách nhau bởi một dấu cách. Mỗi xâu chỉ gồm các chữ cái la tinh in thường và có độ dài không vượt quá $50$.

## Kết quả

- Với mỗi cặp $A$, $B$, ghi ra trên một dòng: `similar` nếu chúng tương tự, ngược lại ghi `not similar`.

## Ví dụ

### Sample input 1
```
5
apple applee
apple appe
apple bpple
applee bpple
apple apple
```
### Sample output 1
```
similar
similar
similar
not similar
similar
```

Ba cặp đầu tương tự nhau lần lượt qua thao tác chèn, xoá và đổi một ký tự; cặp `applee` và `bpple` cần tới hai thao tác nên không tương tự; cặp cuối gồm hai xâu giống hệt nhau nên tương tự.
