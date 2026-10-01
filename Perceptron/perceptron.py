#chúng ta sử dụng numpy cho phép toán ma trận (matrix operations) để giữ mọi thứ tối giản
import numpy as np

#xác định Perceptron class: chúng tôi sẽ xây dựng perceptron giống 1 class để giữ mọi thứ được tổ chức. class sẽ bao gồm các phương thức training và prediction

class Perceptron:
    def __init__(self, learning_rate=0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

#method fit huấn luyện model bằng cách điều chính trọng số (weights) và hệ số tự do (bias) mỗi khi modek không phân loại được điểm (point)
    def fit(self, X, y):
        #Number of samples and features
        n_samples, n_features = X.shape

        #Initialize weights and bía
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