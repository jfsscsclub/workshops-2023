# Code by Mostafa Hussein, comments by Tony Lin, special thanks to Aritro Saha for helping with comments
import tensorflow as tf
import tensorflow.keras.layers as layers
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist

(xTraining, yTraining),(xTesting, yTesting) = mnist.load_data("mnist.npz")

# reshape to fit tensor (unit that contains data)
# 28x28 image
xTraining = xTraining.reshape(60000, 28, 28, 1)
# remove colour 
xTraining = xTraining / 255.0

# defining our own model
model = tf.keras.models.Sequential([
    # filters the data, and is modifiable by the NN so it can decide which parts are important
    layers.Conv2D(64, (3,3), activation = 'relu', input_shape = (28,28,1)),
    # downsample part, groups 4x4 section of data and takes the max of each corner, leading to a 2x2 square of outputs
    layers.MaxPooling2D(2,2),
    # repeat one more time
    layers.Conv2D(64, (3,3), activation = 'relu', input_shape = (28,28,1)),
    layers.MaxPooling2D(2,2),
    # make it into a 1d array
    layers.Flatten(),
    # actual NN part
    # hidden layers
    # each layer contains nodes, which the NN can control and modify what each node does
    # connects together like a neurons in a brain, where each can interconnect to another and influence its outputs
    layers.Dense(200, activation = "relu"),
    layers.Dense(100, activation = "relu"),
    # output layer, takes input from the second last layer and outputs 0-9
    layers.Dense(10, activation = "softmax")
])

model.summary()

# will run everytime it trains / validates, stops it if it is very accurate, saving time
class myCallBack(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs = {}):
    if (logs.get('accuracy') != None):
      if (logs.get('accuracy') >= 0.99):
        print("Model stopped training, since accuracy is above 99.8%.")
        self.model.stop_training = True

# start training the model
# configure the model to use specific alghorithms to determine its loss, and how to optimize it etc
model.compile(optimizer= "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
# actual training
model.fit(
    # data we're using to train
    xTraining,
    yTraining,
    # number of iterations to try
    epochs = 20,
    # calling our custom callback every time
    callbacks = [myCallBack()]
)

# saving our model 
model.save("/Meeting14-IntroToML/Model_1")
# test out our model with an image
img = tf.keras.preprocessing.image.load_img("num9.png", color_mode = "grayscale", target_size = (28,28 , 1))
plt.imshow(img)
# convert it to array
imgArr = tf.keras.preprocessing.image.img_to_array(img)
# change to np array
imgArr = np.array([imgArr])
# model tries to predict image
prediction = model.predict(imgArr)
print(prediction)
