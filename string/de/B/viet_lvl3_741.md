# Bộ kiểm tra số nguyên

## Mô tả đề bài

Ta cần xây dựng một bộ kiểm tra để xác định một "số" $x$ cho trước có hợp lệ hay không. Số $x$ được coi là **hợp lệ** khi đồng thời thoả mãn hai điều kiện:

- **Đúng định dạng:** một số nguyên đúng định dạng hoặc bằng `0`, hoặc gồm một dấu trừ `-` (có thể có hoặc không), tiếp theo là một chữ số từ `1` đến `9`, rồi đến một dãy (có thể rỗng) các chữ số từ `0` đến `9`. Nói cách khác, ngoài chính số `0`, mọi số nguyên đều không được có chữ số `0` ở đầu, và cũng không có dạng `-0`.
- **Nằm trong đoạn:** $l \le x \le r$.

Cho $l$, $r$ và $T$ số cần kiểm tra, với mỗi $x$ hãy đưa ra kết quả kiểm tra tương ứng.

## Dữ liệu

- Dòng đầu tiên chứa ba số nguyên $l$, $r$, $T$ — đoạn kiểm tra $[l, r]$ và số lượng số cần kiểm tra ($0 \le T \le 512$; $l$, $r$ nằm trong phạm vi số nguyên có dấu $64$ bit, tức $-2^{63} \le l \le r \le 2^{63} - 1$).
- $T$ dòng tiếp theo, mỗi dòng chứa một xâu $x$ cần kiểm tra. Bảo đảm $x$ có độ dài ít nhất $1$, chỉ gồm các ký tự `0`–`9` và `-`, dấu `-` nếu có chỉ xuất hiện ở vị trí đầu tiên. Lưu ý $x$ có thể dài hơn nhiều so với sức chứa của kiểu $64$ bit.

## Kết quả

- Gồm $T$ dòng, mỗi dòng một số nguyên là kết quả kiểm tra của $x$ tương ứng: `0` nếu $x$ hợp lệ; `1` nếu $x$ sai định dạng; `2` nếu $x$ đúng định dạng nhưng nằm ngoài đoạn $[l, r]$.

## Ví dụ

### Sample input 1
```
-3 3 4
0
00
-0
100000000000000000000
```
### Sample output 1
```
0
1
1
2
```

Số `0` đúng định dạng và thuộc đoạn $[-3, 3]$ nên cho `0`. Hai số `00` và `-0` đều sai định dạng vì có chữ số `0` ở đầu nên cho `1`. Số `100000000000000000000` đúng định dạng nhưng lớn hơn $3$ nên cho `2`.
