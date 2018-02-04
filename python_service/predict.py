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
    if model_name == "number":
        im = pre.processImage("prediction_images/" + model_name + "/temp.jpg",8,8)
    else:
        im = pre.processImage("prediction_images/" + model_name + "/temp.jpg",100,100)
    prediction = model.predict(im.reshape(-1,1).T)
    
    return prediction

