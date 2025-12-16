# define inputs and outputs
X = [(0,0),(1,0),(0,1),(1,1)]
and_y = [0,0,0,1]
or_y = [0,1,1,1]
nor_y = [1,0,0,0]
nand_y = [1,1,1,0]

# initalie some random weights
w1,w2,b = 0.2,-0.1,0
learning_rate = 0.1

# activation function
def activation(x):
  return 1 if x>=0 else 0

# design the forward pass
def forward(x1,x2,w1,w2,b):
  val = x1*w1 + x2*w2 + b
  return activation(val)

# train the model
# epoch:1 ; batch:4
def train(X,y,learning_rate,epochs):
  global w1,w2,b
  # iterate through each epoch
  for epch in range(epochs):
    # iterate through each batch
    for i in range(len(y)):
      x1,x2 = X[i]
      target = y[i]
      
      out = forward(x1,x2,w1,w2,b)
      # compute error
      E = target - out
      # update weights and bias
      w1 = w1 + learning_rate*E*x1
      w2 = w2 + learning_rate*E*x2
      b = b + learning_rate*E

def test(X,y,w1,w2,b):
  mse = 0
  # iterate through each batch
  # MSE = 1/n sigma (y-y_pred)**2
  for i in range(len(y)):
    x1,x2 = X[i]
    target = y[i]
    out = forward(x1,x2,w1,w2,b)
    # update MSE
    mse += (target-out)**2
  mse = mse/len(y)
  return mse

# show the output
train(X,and_y,learning_rate,1)
print(f"AND gate updated weights: w1 = {w1}, w2 = {w2}, b = {b}")
print(f"MSE for AND gate: {test(X,and_y,w1,w2,b)}")

w1,w2,b = 0.2,-0.1,0
train(X,or_y,learning_rate,1)
print(f"OR gate updated weights: w1 = {w1}, w2 = {w2}, b = {b}")
print(f"MSE for OR gate: {test(X,or_y,w1,w2,b)}")

w1,w2,b = 0.2,-0.1,0
train(X,nand_y,learning_rate,1)
print(f"NAND gate updated weights: w1 = {w1}, w2 = {w2}, b = {b}")
print(f"MSE for NAND gate: {test(X,nand_y,w1,w2,b)}")

w1,w2,b = 0.2,-0.1,0
train(X,nor_y,learning_rate,1)
print(f"NOR gate updated weights: w1 = {w1}, w2 = {w2}, b = {b}")
print(f"MSE for NOR gate: {test(X,nor_y,w1,w2,b)}")



'''
AND gate updated weights: w1 = 0.2, w2 = 0.0, b = -0.1
MSE for AND gate: 0.25
OR gate updated weights: w1 = 0.2, w2 = 0.0, b = 0.0
MSE for OR gate: 0.25
NAND gate updated weights: w1 = 0.1, w2 = -0.1, b = 0.0
MSE for NAND gate: 0.5
NOR gate updated weights: w1 = 0.1, w2 = -0.1, b = -0.1
MSE for NOR gate: 0.5
'''
