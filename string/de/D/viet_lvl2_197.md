# Phân loại từ theo chữ cái

## Mô tả đề bài

Để học từ vựng hiệu quả hơn, ta muốn gom các từ thành từng nhóm. Hai từ được xếp vào **cùng một nhóm** khi và chỉ khi số lần xuất hiện của mỗi chữ cái trong hai từ đều bằng nhau (nói cách khác, từ này là một cách đảo thứ tự các chữ cái của từ kia).

Ví dụ, `AABAC` và `CBAAA` được xếp cùng một nhóm (cả hai đều gồm ba chữ `A`, một chữ `B`, một chữ `C`), còn `AABAC` và `AAABB` thì không.

Cho $N$ từ, tất cả đều gồm các chữ cái la tinh in hoa. Hãy cho biết các từ này được chia thành bao nhiêu nhóm.

## Dữ liệu

- Dòng thứ nhất: số nguyên $N$ ($1 \le N \le 10^4$) — số lượng từ.
- $N$ dòng tiếp theo, mỗi dòng chứa một từ gồm các chữ cái la tinh in hoa, độ dài không vượt quá $100$.

## Kết quả

- Một dòng duy nhất chứa một số nguyên là số nhóm mà $N$ từ được chia thành.

## Ví dụ

### Sample input 1
```
3
AABAC
CBAAA
AAABB
```
### Sample output 1
```
2
```

Hai từ `AABAC` và `CBAAA` thuộc cùng một nhóm vì có cùng thành phần chữ cái, còn `AAABB` thuộc một nhóm riêng; tổng cộng có $2$ nhóm.
