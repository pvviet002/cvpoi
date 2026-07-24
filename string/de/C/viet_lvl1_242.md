# Cắt bỏ hậu tố

## Mô tả đề bài

Cho một từ. Nếu từ đó kết thúc bằng một trong các hậu tố `er`, `ly` hoặc `ing` thì hãy xoá đúng một lần hậu tố đó và in ra phần còn lại; ngược lại, giữ nguyên từ. Dữ liệu bảo đảm sau khi xoá hậu tố, từ vẫn còn ít nhất một chữ cái.

## Dữ liệu

- Một dòng duy nhất chứa một từ gồm các chữ cái, không chứa dấu cách, độ dài không vượt quá $32$.

## Kết quả

- In ra từ sau khi đã xử lý theo quy tắc trên.

## Ví dụ

### Sample input 1
```
singing
```
### Sample output 1
```
sing
```

Từ `singing` kết thúc bằng hậu tố `ing`, sau khi cắt bỏ một lần còn lại `sing`.
