Mạng perceptron hoạt động như sau:

- **Input**: Là một mảng gồm các số thực [a, b, c, d]
- **Output**: Trả về số 1 hoặc 0 dựa trên điều kiện so sánh.

Tuy nhiên, thay vì người lập trình phải tự viết cứng công thức if `a + b + c> d`, mạng Perceptron sẽ tự gắn các trọng số [w1, w2, w3, w4] và một số thiên vị b vào các biến. Qua quá trình học, nó sẽ tự dò ra công thức so sánh đó để cho ra Output 1 hoặc 0 chính xác nhất.

//https://dev.to/dazevedo/implementing-a-perceptron-from-scratch-in-python-1j41

### Perceptron là gì?

- Perceptron là một thuật toán cơ bản dành cho học có giám sát của các bộ phân lớp nhị phân. Được cho các đặc trưng đầu vào, Perceptron học các trọng số (weights) có tác dụng chia các lớp dựa trên hàm threshold cơ bản. Đây là cách nói đơn giản về hoạt động của nó:
  - Input: một vector đặc trưng (ví dụ: [x1, x2])
  - Weights: mỗi đặc trưng đầu vào đề có trọng số -
