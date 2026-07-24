# Giải nén ảnh điểm

## Mô tả đề bài

Một bức ảnh đen trắng được biểu diễn bằng một ma trận nhị phân kích thước $N \times N$, mỗi ô mang giá trị `0` hoặc `1`. Đọc lần lượt các ô theo từng dòng từ trên xuống dưới, trong mỗi dòng đọc từ trái sang phải, ta thu được một dãy gồm $N \times N$ ký tự nhị phân. Dãy này gồm nhiều đoạn liên tiếp các ký tự giống nhau.

Để nén ảnh, người ta ghi lại: số đầu tiên là $N$; sau đó là độ dài của các đoạn liên tiếp, trong đó đoạn đầu tiên gồm các ký tự `0`, đoạn thứ hai gồm các ký tự `1`, đoạn thứ ba lại gồm các ký tự `0`, cứ thế xen kẽ. Nếu ảnh bắt đầu bằng ký tự `1` thì độ dài đoạn `0` đầu tiên được ghi là $0$.

Cho mã nén, hãy khôi phục và in ra ma trận nhị phân $N \times N$ ban đầu.

## Dữ liệu

- Một dòng gồm các số nguyên cách nhau bởi dấu cách, biểu diễn mã nén. Số đầu tiên là $N$ ($3 \le N \le 200$), các số tiếp theo là độ dài các đoạn xen kẽ.

## Kết quả

- In ra $N$ dòng, mỗi dòng gồm $N$ ký tự `0` hoặc `1`, là ma trận sau khi giải nén. Giữa các ký tự không có dấu cách.

## Ví dụ

### Sample input 1
```
7 3 1 6 1 6 4 3 1 6 1 6 1 3 7
```
### Sample output 1
```
0001000
0001000
0001111
0001000
0001000
0001000
1111111
```

Ma trận khôi phục có kích thước $7 \times 7$, đúng bằng dãy $49$ ký tự mà mã nén mô tả.
