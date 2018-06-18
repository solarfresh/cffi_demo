
import numpy as np
from keras.datasets import mnist
from os import path
from PIL import Image

file_dir = path.join(path.dirname(path.abspath(__file__)), '../images')
(x_train, y_train), (x_test, y_test) = mnist.load_data()
for idx, img_array in enumerate(x_test):
    if idx >= 5:
        break
    img = Image.fromarray(img_array)
    img.save(path.join(file_dir, 'image' + str(idx) + '.jpg'))
