'''
Write Python code for sigmoid activation and its derivative.
Test both for input x = 0.5.
'''

import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s*(1-s)

x = 0.5
sig = sigmoid(x)
sig_der = sigmoid_derivative(x)
print(f"Sigmoid({x}) = {sig}")
print(f"Sigmoid Derivative({x}) = {sig_der}")
