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


    im = pre.processImage("prediction_images/" + model_name + "/temp.jpg",8 ,8)

    prediction = model.predict(im.reshape(1,-1))

    return str(predictions[0])
