# Tách theo dấu phẩy

## Mô tả đề bài

Cho một dòng gồm các trường được ngăn cách bởi dấu phẩy `,`. Hãy in ra mỗi trường trên một dòng riêng theo thứ tự, kể cả những trường rỗng (khi hai dấu phẩy đứng liền nhau, hoặc dấu phẩy ở đầu, ở cuối dòng). Sau đó in số lượng trường.

## Dữ liệu

- Một dòng duy nhất chứa các trường ngăn cách bởi dấu phẩy, độ dài không vượt quá $1000$. Mỗi trường không chứa dấu cách.

## Kết quả

- Mỗi trường in trên một dòng riêng theo thứ tự (trường rỗng in ra một dòng trống).
- Dòng cuối cùng là số lượng trường.

## Ví dụ

### Sample input 1
```
an,binh,,cuong
```
### Sample output 1
```
an
binh

cuong
4
```

Giữa `binh` và `cuong` có một trường rỗng, nên có tất cả $4$ trường.
