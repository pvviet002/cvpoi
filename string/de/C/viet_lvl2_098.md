# Đếm số lần xuất hiện của từ

## Mô tả đề bài

Nhiều trình soạn thảo văn bản có chức năng tìm kiếm từ, giúp xác định nhanh vị trí của một từ trong đoạn văn và đếm số lần từ đó xuất hiện.

Cho một từ và một đoạn văn, hãy đếm số lần từ đó xuất hiện trong đoạn văn và cho biết vị trí xuất hiện đầu tiên. Khi so khớp, không phân biệt chữ hoa và chữ thường, nhưng phải khớp trọn vẹn: từ cần tìm phải trùng khít với một từ độc lập trong đoạn văn; nếu từ cần tìm chỉ là một phần của một từ nào đó trong đoạn văn thì không được tính là khớp.

Các từ trong đoạn văn được ngăn cách bởi dấu cách. Vị trí được tính từ $0$, trong đó mỗi dấu cách cũng chiếm một vị trí.

## Dữ liệu

- Dòng đầu tiên chứa một xâu chỉ gồm chữ cái, là từ cần tìm; độ dài từ $1$ đến $10$.
- Dòng thứ hai chứa một xâu chỉ gồm chữ cái và dấu cách, là đoạn văn; độ dài từ $1$ đến $10^6$.

## Kết quả

- Nếu tìm thấy từ trong đoạn văn, in ra hai số nguyên cách nhau bởi một dấu cách: số lần từ xuất hiện và vị trí mà chữ cái đầu của từ xuất hiện lần đầu trong đoạn văn.
- Nếu từ không xuất hiện, in ra một số nguyên $-1$.

## Ví dụ

### Sample input 1
```
To
to be or not to be is a question
```
### Sample output 1
```
2 0
```

### Sample input 2
```
to
Did the Ottoman Empire lose its power at that time
```
### Sample output 2
```
-1
```

Ở ví dụ thứ nhất, từ `to` xuất hiện $2$ lần với tư cách là từ độc lập, lần đầu ngay tại vị trí $0$. Ở ví dụ thứ hai, `to` chỉ nằm bên trong một từ khác nên không được tính là khớp trọn vẹn.
