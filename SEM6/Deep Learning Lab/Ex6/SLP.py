# Single layer perceptron for AND logic gate

import tensorflow as tf
import numpy as np

X = np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y = np.array([[0.],[0.],[0.],[1.]])

model = tf.keras.Sequential([tf.keras.layers.Dense(1,activation='sigmoid',input_shape=(2,))])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
    loss='binary_crossentropy'
)

model.fit(X, y, epochs=10)

predictions = model.predict(X)
print("Predictions:")
print(predictions)

binary_predictions = (predictions >= 0.5).astype(int)

print("Binary Predictions:")
print(binary_predictions)
