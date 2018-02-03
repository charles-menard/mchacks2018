import pandas as pd
import numpy as np
import os
from PIL import Image

def resize(filename, height, width):
    im = Image.open(filename)
    return im.resize((height,width), Image.BILINEAR)

def toGrey(image):
    return image.convert('L')

def processImage(filename, height, width):
    return np.array(toGrey(resize(filename, height, width)))

# heigth width c'est le size qu'on resize les images
def fetchImage(nameOfModel, height=100, width=100):
    X = pd.DataFrame()
    y = []
    for classes in os.listdir("../models/"+ nameOfModel + "/"):
        for imgName in os.listdir("../models/"+ nameOfModel + "/" + classes):
            imagearr = processImage("../models/"+nameOfModel+"/"+classes+"/"+imgName,
                                            height, width)
            X = X.append(imagearr)
            y = y + [classes]
    y = np.array(y).T
    return X,y

X,y = fetchImage("testmodel")
print(X)
print(y)
