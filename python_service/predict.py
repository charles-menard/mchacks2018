from saver import Saver
from preprocess_img import Preprocessor
from PIL import Image
import urllib.request
import io
import numpy as np

def pred(model_name="number"):
    pre = Preprocessor()
    #loading the pickle
    sav=Saver()
    model = sav.load("trained_models/", model_name+ "_model")

    #preprocessing of images
    im = pre.processImage("prediction_images/" + model_name + "/temp.jpg")

    

    return model.predict(im.reshape(-1,1).T)
