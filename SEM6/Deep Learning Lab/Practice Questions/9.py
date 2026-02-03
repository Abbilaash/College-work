'''
Implement a single-layer perceptron from scratch to classify the AND gate.
i. Inputs: (0,0), (0,1), (1,0), (1,1)
ii. Train for 10 epochs
iii. Print final weights and bias
iv. Final predictions
'''

import math

x = [(0,0), (0,1), (1,0), (1,1)]
y = [0,0,0,1]
w1,w2,b = 0.2,0.3,0.1
learning_rate = 0.1
epochs = 10

def activation(x):
    return 1 if x>=0 else 0

def perceptron(x1,x2,w1,w2,b):
    return activation(w1*x1+w2*x2+b)

def train(x,y,learning_rate,epochs):
    global w1,w2,b,out
    for j in range(epochs):
        if j==epochs-1:
            print("Final Predictions:")
        for i in range(len(y)):
            x1,x2 = x[i]
            target = y[i]
            out = perceptron(x1,x2,w1,w2,b)
            if j==epochs-1:
                print(out)
            E = target-out
            w1=w1+learning_rate*E*x1
            w2=w2+learning_rate*E*x2
            b=b+learning_rate*E

print(f"Before updation: w1={w1}, w2={w2}, b={b}")
train(x,y,learning_rate,epochs)
print(f"After updation: w1={w1}, w2={w2}, b={b}")
