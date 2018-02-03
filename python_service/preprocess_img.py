# Import
from sklearn.decomposition import PCA
from PIL import Image
import numpy as np
class Preprocessor:
    def __init__(self):
        self.pre = "initiated"

    def resize(self, filename, height, width):
        im = Image.open(filename)
        return im.resize((height,width), Image.NEAREST)

    def toGrey(self, image):
        return image.convert('L')

    def processImage(self, filename, height, width):
        im = np.array(self.toGrey(self.resize(filename, height, width)))
        return im.flatten()


    #pca
    def pca_data(self, data,variance=0.50):
        pca = PCA(variance).fit(data)
        components = pca.transform(data)
        return components
