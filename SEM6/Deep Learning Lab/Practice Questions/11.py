'''
Implement one step of backpropagation for XOR gate. 
- compute output error
- update output layer weights
'''

import math

X = [(1,1)]
y = [0]
learning_rate = 0.1
v1,v2=0.3,0.4
w11,w12,w21,w22,b,w31,w32=0.5,0.4,0.5,0.6,0.1,0.2,0.1

def activation(x):
    return 1 if x>=0 else 0

def train(X,y,learning_rate):
    global w11,w12,w21,w22,b,w31,w32,v1,v2
    x1,x2 = X[0]
    y = y[0]

    h1 = activation(w11*x1+w21*x2+w31)
    h2 = activation(w12*x1+w22*x2+w32)
    y_pred = activation(v1*h1+v2*h2+b)

    mse = (y-y_pred)**2
    print(f"Mean Squared Error before backpropagation: {mse:.4f}")

    del_out = -2*(y-y_pred)*y_pred*(1-y_pred)
    del_h1 = del_out*v1*h1*(1-h1)
    del_h2 = del_out*v2*h2*(1-h2)

    v1_new = v1-learning_rate*del_out*h1
    v2_new = v2-learning_rate*del_out*h2

    w11_new = w11-learning_rate*del_h1*x1
    w12_new = w12-learning_rate*del_h1*x2
    w21_new = w21-learning_rate*del_h2*x1
    w22_new = w22-learning_rate*del_h2*x2
    w31_new = w31-learning_rate*del_h1
    w32_new = w32-learning_rate*del_h2
    b = b-learning_rate*del_out

    h1 = activation(w11*x1+w21*x2+w31)
    h2 = activation(w12*x1+w22*x2+w32)
    y_pred = activation(v1*h1+v2*h2+b)

    mse = (y-y_pred)**2
    print(f"Mean Squared Error after backpropagation: {mse:.4f}")

train(X,y,learning_rate)
