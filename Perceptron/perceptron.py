#chúng ta sử dụng numpy cho phép toán ma trận (matrix operations) để giữ mọi thứ tối giản
import numpy as np

#xác định Perceptron class: chúng tôi sẽ xây dựng perceptron giống 1 class để giữ mọi thứ được tổ chức. class sẽ bao gồm các phương thức training và prediction

class Perceptron:
    def __init__(self, learning_rate=0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

#method fit huấn luyện model bằng cách điều chính trọng số (weights) và hệ số tự do (bias) mỗi khi model không phân loại được điểm (point)
    def fit(self, X, y):
        #Number of samples and features
        n_samples, n_features = X.shape

        #Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0

        #Training
        for _ in range(self.epochs):
            for idx, x_i in enumerate(X):
                #Calculate linear output
                linear_output = np.dot(x_i, self.weights) + self.bias
                #Apply step function
                y_predicted = self._step_function(linear_output)

                #Update weights and bias if there is a missclassification
                if y[idx] != y_predicted:
                    update = self.learning_rate* (y[idx] - y_predicted)
                    self.weights += update * x_i
                    self.bias += update

#method predict tính toán dự đoán ở trên data mới
    def predict(self, X):
        #calculate linear output and apply step function
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self._step_function(linear_output)
        return y_predicted

#method step_function áp dụng ngưỡng (threshold) xác định output class
    def _step_function(self, x):
        return np.where(x >=0, 1, 0)

#AND gate dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1]) #Labels for AND gate

#Initialze Perceptron
p = Perceptron(learning_rate=0.1, epochs=10)

#Train the model
p.fit(X,y)

#Test the model
print("Predictions:", p.predict(X))

# giải thích quá trình học của perceptron
# giải thích cấu hình khởi tạo: khởi tạo weights và bias bằng 0, điều này cho phép model bắt đầu học từ cơ bản.
# tính toán linear_output: với mỗi điểm dữ liệu, perceptron tính toán tổng có trọng số của inputs và cộng với hệ số tự do
# activation (step function): nếu linear output lớn hơn hoặc bằng 0, gán với class 1, nếu không gán với class 0
# update rule: nếu như dự đoán không chính xác, model sẽ điều chỉnh trọng số và hệ số tự do theo hướng giảm error. Update rule như sau: weights += learning_rate*(y_true - y_pred) * x
# điều này giúp Perceptron chỉ update các điểm dữ liệu sai phân loại, dần dần đảy mô hình gần với ranh giới quyết định (decision boundary) chính xác.

#visualizing decision boundaries: trực quan hóa ranh giới quyết định sau khi training. Điều này đặc biệt giúp ích khi bạn làm việc với các datasets phức tạp. Từ bây giờ, chúng tôi sẽ giữ mọi thứ đơn giản với AND gate.

#mở rộng ra với MLP (Multi-Layer Perceptrons): mặc dù perceptron chỉ giới hạn ở các vấn đề phân chia tuyến tính, nó là nền tảng của các mạng neural phức tạp hơn như Multi Layer Perceptrons (MLPs). Với MLPs, chúng tôi sẽ thêm một vài hidden layer và hàm kích hoạt (như ReLU hoặc Sigmoid) để giải quyết các vấn đề phi tuyến

#tổng kết: Perceptron là một thuật toán đơn giản nhưng nền tảng. Bằng cách hiểu perceptron hoạt động