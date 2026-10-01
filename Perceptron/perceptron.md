Mạng perceptron hoạt động như sau:

- **Input**: Là một mảng gồm các số thực [a, b, c, d]
- **Output**: Trả về số 1 hoặc 0 dựa trên điều kiện so sánh.

Tuy nhiên, thay vì người lập trình phải tự viết cứng công thức if `a + b + c> d`, mạng Perceptron sẽ tự gắn các trọng số [w1, w2, w3, w4] và một số thiên vị b vào các biến. Qua quá trình học, nó sẽ tự dò ra công thức so sánh đó để cho ra Output 1 hoặc 0 chính xác nhất.

https://dev.to/dazevedo/implementing-a-perceptron-from-scratch-in-python-1j41

### Perceptron là gì?

- **Perceptron** là một thuật toán cơ bản dành cho học có giám sát của các bộ phân lớp nhị phân. Được cho các đặc trưng đầu vào, Perceptron học các trọng số (weights) có tác dụng chia các lớp dựa trên hàm threshold (hàm giới hạn, hàm ngưỡng, nếu đầu vào thấp hơn ngưỡng trả về 0 hoặc -1; nếu đầu vào vượt quá ngưỡng trả về 1) cơ bản. Đây là cách nói đơn giản về hoạt động của nó:
  - **Input**: một vector đặc trưng (ví dụ: [x1, x2])
  - **Weights**: mỗi đặc trưng đầu vào có một trọng số, trọng số này được mô hình điều chỉnh tùy thuộc vào mức độ hoạt động của mô hình.
  - **Activation Function (hàm kích hoạt)**: tính toán tổng có trọng số của các đặc trưng đầu vào và áp dụng ngưỡng để quyết định kết quả thuộc class nào.

- Về mặt toán học, nó sẽ trông như sau:
  `f(x) = w1*x1 + w2*x2 + ... + wn*xn + b`
  Trong đó:
  - `f(x)` là output
  - `w` biểu diễn trọng số
  - `x` biểu diễn các đặc trưng đầu vào
  - `b` là hệ số tự do

  Nếu `f(x)` lớn hơn hoặc = với threshold (ngưỡng), output là class 1, nếu không, output là class 0
