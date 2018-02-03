from PIL import Image
from skimage import color
import matplotlib
import numpy as np


def resize(filename, height, width):
    im = Image.open(filename)
    return im.resize((height,width), Image.NEAREST)

def toGrey(image):
    return image.convert('L')

def processImage(filename, height, width):
    return np.array(toGrey(resize(filename, height, width)))
