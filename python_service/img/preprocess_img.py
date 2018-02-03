# Import
from sklearn.decomposition import PCA
from PIL import Image
import numpy as np

def resize(filename, height, width):
    im = Image.open(filename)
    return im.resize((height,width), Image.BILINEAR)

def toGrey(image):
    return image.convert('L')

def processImage(filename, height, width):
    return np.array(toGrey(resize(filename, height, width)))


#pca
def pca_data(data,variance=0.50):
    pca = PCA(variance).fit(data)
    components = pca.transform(data)
    return components
