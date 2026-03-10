import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.applications import VGG16
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

IMG_SIZE = (32, 32)
BATCH_SIZE = 64
EPOCHS = 20
NUM_CLASSES = 10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)

def create_lenet():
    model = Sequential([
        Conv2D(6, kernel_size=(5,5), activation='relu', input_shape=(32,32,3), padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(16, kernel_size=(5,5), activation='relu'),
        MaxPooling2D(pool_size=(2,2)),
        Flatten(),
        Dense(120, activation='relu'),
        Dense(84, activation='relu'),
        Dense(NUM_CLASSES, activation='softmax')
    ])
    
    model.compile(optimizer=Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

def create_alexnet():
    model = Sequential([
        Conv2D(96, kernel_size=(3,3), strides=(1,1), activation='relu', input_shape=(32,32,3), padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(256, kernel_size=(3,3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(384, kernel_size=(3,3), activation='relu', padding='same'),
        Conv2D(384, kernel_size=(3,3), activation='relu', padding='same'),
        Conv2D(256, kernel_size=(3,3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(NUM_CLASSES, activation='softmax')
    ])
    
    model.compile(optimizer=Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

def create_vgg16():
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32,32,3))
    
    base_model.trainable = False
    
    x = Flatten()(base_model.output)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    outputs = Dense(NUM_CLASSES, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=outputs)
    
    model.compile(optimizer=Adam(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

models = {
    'LeNet': create_lenet(),
    'AlexNet': create_alexnet(),
    'VGG16': create_vgg16()
}

histories = {}

for name, model in models.items():
    print(f"\nTraining {name}...")
    history = model.fit(x_train, y_train,epochs=EPOCHS,batch_size=BATCH_SIZE,validation_split=0.2,verbose=1)
    histories[name] = history

for name, history in histories.items():
    plt.plot(history.history['val_accuracy'], label=f'{name}')

plt.title("Validation Accuracy Comparison")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

for name, model in models.items():
    loss, acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"{name} Test Accuracy: {acc:.4f}")
