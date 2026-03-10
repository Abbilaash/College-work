import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("tested.csv")

data = data[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

data['Sex'] = data['Sex'].map({'male':0,'female':1})
data = pd.get_dummies(data, columns=['Embarked'])

X = data.drop('Survived', axis=1)
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def create_model(optimizer):

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model


# Train With SGD
model_sgd = create_model(tf.keras.optimizers.SGD(learning_rate=0.01))

history_sgd = model_sgd.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

# Train With RMSProp
model_rms = create_model(tf.keras.optimizers.RMSprop(learning_rate=0.001))

history_rms = model_rms.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

# Train With Adam
model_adam = create_model(tf.keras.optimizers.Adam(learning_rate=0.001))

history_adam = model_adam.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

plt.plot(history_sgd.history['loss'], label='SGD')
plt.plot(history_rms.history['loss'], label='RMSProp')
plt.plot(history_adam.history['loss'], label='Adam')

plt.title("Optimizer Comparison (MLP on Titanic Dataset)")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

print("SGD Accuracy:", model_sgd.evaluate(X_test, y_test)[1])
print("RMSProp Accuracy:", model_rms.evaluate(X_test, y_test)[1])
print("Adam Accuracy:", model_adam.evaluate(X_test, y_test)[1])



'''
OUTPUT:

3/3 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.5952 - loss: 0.6766
SGD Accuracy: 0.5952380895614624
3/3 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.5952 - loss: 0.6749
RMSProp Accuracy: 0.5952380895614624
3/3 ━━━━━━━━━━━━━━━━━━━━ 0s 8ms/step - accuracy: 0.5952 - loss: 0.6750
Adam Accuracy: 0.5952380895614624
'''

