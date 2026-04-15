# implementing transformer from scratch

'''
Very Simple Transformer (Exam Style)
- Positional Encoding
- Simple Attention
- No complex matrix functions
- Predict next vector
'''

import math

# ---- Data ----
X = [[1,0,1],
     [0,1,1],
     [1,1,0]]

# ---- Positional Encoding (simple) ----
def add_position(X):
    out = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[0])):
            row.append(X[i][j] + (i+1)*0.1)   # simple position
        out.append(row)
    return out

# ---- Dot Product ----
def dot(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))

# ---- Softmax ----
def softmax(arr):
    exp = [math.exp(x) for x in arr]
    s = sum(exp)
    return [e/s for e in exp]

# ---- Attention ----
def attention(X):
    output = []

    for i in range(len(X)):
        scores = []
        
        # compute attention score with all vectors
        for j in range(len(X)):
            score = dot(X[i], X[j]) / math.sqrt(len(X[0]))
            scores.append(score)

        print(f"\nScores for vector {i}:", scores)

        weights = softmax(scores)
        print(f"Weights for vector {i}:", weights)

        # weighted sum
        new_vec = [0]*len(X[0])
        for j in range(len(X)):
            for k in range(len(X[0])):
                new_vec[k] += weights[j] * X[j][k]

        output.append(new_vec)

    return output

# ---- Forward Pass ----
X_pos = add_position(X)

print("Input with Position:")
for row in X_pos:
    print(row)

out = attention(X_pos)

print("\nAttention Output:")
for row in out:
    print(row)

# ---- Predict Next Vector ----
next_vector = out[-1]

print("\nPredicted Next Vector:")
print(next_vector)
