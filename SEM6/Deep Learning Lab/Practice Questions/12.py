'''
Implement MLP for XOR gate for 50 epochs
- print Input->predicted output
'''

import math

X = [(0,0),(0,1),(1,0),(1,1)]
y = [0,1,1,0]
learning_rate = 0.1
v1,v2=0.3,0.4
w11,w12,w21,w22,b,w31,w32=0.5,0.4,0.5,0.6,0.1,0.2,0.1
epochs = 50
h1,h2=None,None

def activation(x):
    return 1 if x>=0 else 0

def train(X,Y,learning_rate,epochs):
    global w11,w12,w21,w22,b,w31,w32,v1,v2,h1,h2

    for i in range(epochs):
        for j in range(len(Y)):
            x1,x2 = X[j]
            y = Y[j]

            h1 = activation(w11*x1+w21*x2+w31)
            h2 = activation(w12*x1+w22*x2+w32)
            y_pred = activation(v1*h1+v2*h2+b)

            del_out = -2*(y-y_pred)*y_pred*(1-y_pred)
            del_h1 = del_out*v1*h1
            del_h2 = del_out*v2*h2

            v1 = v1+learning_rate*del_out*h1
            v2 = v2+learning_rate*del_out*h2

            w11 = w11+learning_rate*del_h1*x1
            w12 = w12+learning_rate*del_h2*x1
            w21 = w21+learning_rate*del_h1*x2
            w22 = w22+learning_rate*del_h2*x2
            w31 = w31+learning_rate*del_h1
            w32 = w32+learning_rate*del_h2
            b = b+learning_rate*del_out

train(X,y,learning_rate,epochs)
for i in range(len(y)):
    x1,x2 = X[i]
    y_pred = activation(v1*h1+v2*h2+b)
    print(f"Input:{x1},{x2} -> Predicted:{y_pred}")
