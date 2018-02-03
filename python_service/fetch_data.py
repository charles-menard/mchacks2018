import pandas as pd
import numpy as np
import os
from preprocess_img import Preprocessor

# heigth width c'est le size qu'on resize les images
def fetchImage(nameOfModel, height, width):
    data = []
    labels = []
    proc = Preprocessor()
    for classes in os.listdir("models/"+ nameOfModel + "/"):
        for imgName in os.listdir("models/"+ nameOfModel + "/" + classes):

            imagearr = proc.processImage("models/"+nameOfModel+"/"+classes+"/"+imgName ,
                                            height, width)
            data = data + [imagearr]
            labels = labels + [classes]
    X = pd.DataFrame(data)
    y = np.array(labels)
    return X,y

X,y = fetchImage("testmodel", 100, 100)
print(X.shape)
print(y.shape)
