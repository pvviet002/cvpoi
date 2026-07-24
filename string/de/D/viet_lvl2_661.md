# Đảo chữ

## Mô tả đề bài

Cho một xâu $S$ gồm các chữ cái la tinh in thường. Ký hiệu $S[i..j]$ là đoạn con của $S$ gồm các ký tự từ vị trí $i$ đến vị trí $j$.

Có $Q$ câu hỏi, mỗi câu hỏi cho bốn số nguyên $A$, $B$, $C$, $D$. Đặt $X = S[A..B]$ và $Y = S[C..D]$. Hãy cho biết có thể sắp xếp lại các chữ cái của $Y$ để thu được đúng xâu $X$ hay không.

## Dữ liệu

- Dòng đầu tiên: xâu $S$ ($1 \le |S| \le 5 \times 10^4$) — chỉ gồm các chữ cái la tinh in thường.
- Dòng thứ hai: số nguyên $Q$ ($1 \le Q \le 5 \times 10^4$) — số câu hỏi.
- $Q$ dòng tiếp theo, dòng thứ $k$ chứa bốn số nguyên $A$, $B$, $C$, $D$ ($1 \le A \le B \le |S|$, $1 \le C \le D \le |S|$) — mô tả câu hỏi thứ $k$.

## Kết quả

- Ghi ra $Q$ dòng, dòng thứ $k$ ghi `YES` nếu câu hỏi thứ $k$ có câu trả lời khẳng định, ghi `NO` trong trường hợp ngược lại.

## Ví dụ

### Sample input 1
```
vodevovode
2
5 8 3 6
2 5 3 6
```
### Sample output 1
```
NO
YES
```

Ở câu hỏi thứ nhất, $X = $ `vovo` còn $Y = $ `devo`. Ở câu hỏi thứ hai, $X = $ `odev` còn $Y = $ `devo`; hai xâu này gồm đúng những chữ cái như nhau.

## Ràng buộc

| Subtask | Điểm | Ràng buộc bổ sung |
| ------- | ---- | ----------------- |
| 1 | 30% | $\lvert S \rvert \le 5000$ và $Q \le 5000$ |
| 2 | 30% | $\lvert S \rvert \le 15000$ và $Q \le 15000$ |
| 3 | 40% | Không có thêm ràng buộc bổ sung |
