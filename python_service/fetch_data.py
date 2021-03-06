import pandas as pd
import numpy as np
import os
from preprocess_img import Preprocessor

# heigth width c'est le size qu'on resize les images
def fetchImage(nameOfModel, height=100, width=100):
    data = []
    labels = []
    listOfLabels = {}
    proc = Preprocessor()
    for i, classes in enumerate(os.listdir("models/"+ nameOfModel + "/")):
        listOfLabels[i] = nameOfModel
        for imgName in os.listdir("models/"+ nameOfModel + "/" + classes):

            imagearr = proc.processImage("models/"+nameOfModel+"/"+classes+"/"+imgName ,
                                            height, width)
            data = data + [imagearr]
            labels = labels + [classes]
    X = pd.DataFrame(data)
    y = np.array(labels)
    return X,y,listOfLabels
