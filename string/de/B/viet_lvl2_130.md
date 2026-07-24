# Đảo ngược chữ số

## Mô tả đề bài

Cho một "số", hãy đảo ngược các chữ số của nó để tạo thành một số mới. Số đã cho có thể thuộc một trong bốn dạng: số nguyên, số thập phân, phân số, hoặc phần trăm. Quy tắc đảo cho từng dạng như sau:

- **Số nguyên:** đảo ngược thứ tự toàn bộ các chữ số.
- **Số thập phân:** đảo ngược phần nguyên, rồi đảo ngược phần thập phân một cách riêng biệt; không hoán đổi vị trí giữa phần nguyên và phần thập phân (dấu chấm giữ nguyên chỗ).
- **Phân số:** đảo ngược tử số và đảo ngược mẫu số một cách riêng biệt; không hoán đổi tử số với mẫu số (dấu gạch phân số giữ nguyên chỗ).
- **Phần trăm:** tử số của phần trăm luôn là số nguyên; chỉ đảo ngược phần chữ số và giữ nguyên dấu `%`.

Quy tắc chuẩn hoá số mới:

- Với một phần nguyên (số nguyên, tử số hoặc mẫu số của phân số, phần chữ số của phần trăm): trừ khi số gốc bằng $0$, chữ số đầu tiên của kết quả sau khi đảo không được là `0` (bỏ các chữ số `0` thừa ở đầu).
- Với phần thập phân: sau khi đảo, không được có chữ số `0` thừa ở cuối (bỏ hết các chữ số `0` ở cuối); nếu phần thập phân toàn chữ số `0` thì chỉ giữ lại đúng một chữ số `0`.
- Phân số không rút gọn; tử số và mẫu số đều không phải số thập phân. Bảo đảm mẫu số khác $0$. Dữ liệu không chứa số âm.

## Dữ liệu

- Một dòng duy nhất chứa số $s$. Nếu $s$ là số nguyên thì có không quá $20$ chữ số; nếu là số thập phân thì phần nguyên và phần thập phân đều không quá $10$ chữ số; nếu là phân số thì tử số và mẫu số đều không quá $10$ chữ số; nếu là phần trăm thì phần chữ số không quá $19$ chữ số.

## Kết quả

- Một dòng duy nhất chứa số đảo ngược của $s$.

## Ví dụ

### Sample input 1
```
5087462
```
### Sample output 1
```
2647805
```

Đảo ngược các chữ số của số nguyên `5087462` được `2647805`.

### Sample input 2
```
600.084
```
### Sample output 2
```
6.48
```

Phần nguyên `600` sau khi đảo và bỏ chữ số `0` thừa ở đầu còn `6`; phần thập phân `084` sau khi đảo và bỏ chữ số `0` thừa ở cuối còn `48`, cho kết quả `6.48`.

### Sample input 3
```
700/27
```
### Sample output 3
```
7/72
```

Tử số `700` đảo còn `7`, mẫu số `27` đảo thành `72`, tử số và mẫu số giữ nguyên vị trí nên được `7/72`.

### Sample input 4
```
8670%
```
### Sample output 4
```
768%
```

Phần chữ số `8670` sau khi đảo và bỏ chữ số `0` thừa ở đầu còn `768`, giữ nguyên dấu `%` được `768%`.
