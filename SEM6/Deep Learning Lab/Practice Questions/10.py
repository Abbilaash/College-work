'''
Implement 2-2-1 MLP for XOR gate
Use Sigmoid as activation function
Loss: MSE
only one forward pass
'''

import math

X = (1,1)
y = [0]
learning_rate = 0.1
v1,v2=0.3,0.4
w11,w12,w21,w22,b,w31,w32=0.5,0.4,0.5,0.6,0.1,0.2,0.1

def activation(x):
    return 1 if x>=0 else 0

def forward(X,y,learning_rate):
    x1,x2 = X
    y = y[0]
    h1 = activation(w11*x1+w21*x2+w31)
    h2 = activation(w12*x1+w22*x2+w32)
    y_pred = activation(v1*h1+v2*h2+b)

    mse = (y-y_pred)**2
    print(f"Mean Squared Error: {mse}")

forward(X,y,learning_rate)
    

