# Đếm xâu con tốt

## Mô tả đề bài

Cho một xâu $s = s_1 s_2 \cdots s_n$ chỉ gồm các chữ số từ `0` đến `9`. Một *xâu con* của $s$ là xâu thu được bằng cách chọn hai chỉ số $l$, $r$ ($1 \le l \le r \le n$) rồi lấy tất cả các ký tự từ vị trí $l$ đến vị trí $r$: $s' = s_l s_{l+1} \cdots s_r$.

Ta gọi một xâu số $p = p_1 p_2 \cdots p_m$ là **không giảm liền bậc** nếu với mọi $i$ thoả $1 < i \le m$ đều có $p_i = p_{i-1}$ hoặc $p_i = p_{i-1} + 1$; nghĩa là mỗi chữ số hoặc bằng chữ số ngay trước nó, hoặc lớn hơn chữ số ngay trước nó đúng $1$ đơn vị. Ví dụ, `12233` và `456` là các xâu không giảm liền bậc.

Một xâu con được gọi là *xâu tốt* nếu nó thoả mãn một trong hai điều kiện:

1. Xâu con có độ dài $1$ thì luôn là xâu tốt.
2. Xâu con có độ dài lớn hơn $1$ và có thể tách thành **hai đoạn liên tiếp**, mỗi đoạn là một xâu không giảm liền bậc.

Hãy đếm xem trong tất cả các xâu con của $s$ có bao nhiêu xâu con là xâu tốt.

## Dữ liệu

- Một dòng duy nhất chứa xâu $s$ chỉ gồm các chữ số từ `0` đến `9`, độ dài $n$ thoả $1 \le n \le 10^5$.

## Kết quả

- Một dòng duy nhất chứa một số nguyên là số xâu con tốt. Kết quả có thể rất lớn nên cần dùng kiểu số nguyên $64$ bit.

## Ví dụ

### Sample input 1
```
12258
```
### Sample output 1
```
12
```

### Sample input 2
```
97856
```
### Sample output 2
```
13
```

Với xâu `12258`, các xâu con tốt gồm: $5$ xâu độ dài $1$ (`1`, `2`, `2`, `5`, `8`); $4$ xâu độ dài $2$ (`12`, `22`, `25`, `58`); $2$ xâu độ dài $3$ (`122`, `225`) và $1$ xâu độ dài $4$ (`1225`), tổng cộng $12$ xâu. Với xâu `97856`, tổng số xâu con tốt là $13$.
