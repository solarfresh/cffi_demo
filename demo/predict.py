import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from os import path

model_path = path.join(path.dirname(path.abspath(__file__)), '../models/mnist.h5')
mnist = load_model(model_path)

img_path = path.join(path.dirname(path.abspath(__file__)), '../images', 'image0.jpg')
img = load_img(img_path, target_size=(28, 28), grayscale=True)
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

proba = mnist.predict_proba(img_array, batch_size=1)
print(proba)
