# Số lớn nhất trong văn bản

## Mô tả đề bài

Cho một dòng văn bản gồm nhiều loại ký tự: chữ cái, dấu cách và các ký tự khác, xen lẫn là các con số. Trong văn bản có cả số nguyên lẫn số thực. Hãy tìm số lớn nhất xuất hiện trong dòng văn bản đó.

Quy ước về các số trong văn bản:

- Mọi số đều không mang dấu và không có chữ số `0` thừa ở đầu. Chữ số `0` thừa ở đầu là chữ số `0` có thể lược bỏ ở đầu một số; ví dụ trong `007` có hai chữ số `0` thừa ở đầu, còn chữ số `0` trước dấu chấm trong `0.618` thì không phải. Nghĩa là ngoài số `0`, mọi số nguyên đều có chữ số đầu tiên khác `0`.
- Một số nguyên là một dãy chữ số liền nhau (theo quy ước trên).
- Một số thực là một dãy chữ số có đúng một dấu chấm nằm giữa, hai bên dấu chấm đều phải là chữ số, và phần bên trái dấu chấm là một số nguyên hợp lệ như trên.

## Dữ liệu

- Một dòng duy nhất chứa xâu văn bản, độ dài không quá $10^4$ ký tự. Mỗi số trong văn bản có độ dài không quá $100$ ký tự (kể cả dấu chấm). Bảo đảm hai bên mỗi dấu chấm đều là chữ số và không xuất hiện trường hợp một dãy chữ số có dấu chấm ở cả hai đầu (ví dụ `120.78.90.206` không thể xuất hiện).

## Kết quả

- Một dòng duy nhất là số lớn nhất, in ra đúng nguyên dạng như trong văn bản. Nếu có nhiều số cùng đạt giá trị lớn nhất thì in ra số có độ dài (số ký tự) lớn nhất.

## Ví dụ

### Sample input 1
```
120 315 513 512 153 0
```
### Sample output 1
```
513
```

Các số trong văn bản là $120$, $315$, $513$, $512$, $153$, $0$; lớn nhất là $513$.

### Sample input 2
```
5r2.1q 4p 3.77442qw cock5.0$
```
### Sample output 2
```
5.0
```

Các số trong văn bản là $5$, $2.1$, $4$, $3.77442$, $5.0$; hai số `5` và `5.0` cùng đạt giá trị lớn nhất, trong đó `5.0` có độ dài lớn hơn nên được chọn.
