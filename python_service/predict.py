from saver import Saver
from preprocess_img import Preprocessor
from PIL import Image
from sklearn.datasets import load_digits
import numpy as np

def pred(model_name="number"):
    pre = Preprocessor()
    #loading the pickle
    sav=Saver()
    model = sav.load("trained_models/", model_name+ "_model")

    #preprocessing of images
    #im = pre.processImage("prediction_images/" + model_name + "/temp.jpg",8, 8)

    digits = load_digits()
    data = digits.data
    #prediction = model.predict(im.reshape(-1,1).T)
    prediction = model.predict(data)
    return prediction


print(np.unique(pred()))
