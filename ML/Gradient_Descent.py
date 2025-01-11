import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def gradient_descent(b, w, alpha, points, iterations):
    for i in range(iterations):
        db = 0
        dw = 0
        MSE = 0
        for j in range(len(points)):
            x = points[j][0]
            y = points[j][1]
            y_pred = b + w * x  # Fixed the linear equation error
            db += y_pred - y
            dw += (y_pred - y) * x
            MSE += (y_pred - y) ** 2
        MSE /= len(points)
        b = b - alpha * (db * 2 / len(points))
        w = w - alpha * (dw * 2 / len(points))
        if i%100==0:
            print("Iteration", i, ": b =", b, ", w =", w, ", MSE=", MSE)
    return b, w

data = np.loadtxt(r"C:\Users\yasse\Desktop\ML\Lab1data.txt", delimiter=',')
x=data[:,0].reshape(-1,1)
y=data[:,1].reshape(-1,1)
plt.plot(x,y,'ro', ms=10, mec='k')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

scaler = MinMaxScaler()
Xs = scaler.fit_transform(x)
x = Xs.flatten()
data[:, 0] = x
Ys = scaler.fit_transform(y)
y = Ys.flatten()
data[:, 0] = x
data[:, 1] = y
b,w = gradient_descent(0,0,0.1,data,1000)

y_pred = b+w*x
plt.plot(x,y,'ro', ms=10, mec='k')
plt.plot(x, w * x + b, color='blue')
plt.xlabel("X")
plt.ylabel("Y_Predicted")
plt.show()
