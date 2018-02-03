# Import
from sklearn.decomposition import PCA
from PIL import Image
import numpy as np
class Preprocessor:
    def __init__(self):
        self.pre = "initiated"

    def resize(self, filename, height, width):
        im = Image.open(filename)
        return im.resize((height,width), Image.BILINEAR)

    def toGrey(self, image):
        return image.convert('L')

    def processImage(self, filename, height, width):
        return np.array(toGrey(resize(filename, height, width)))




from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split


def ml_preprocessing(data,labels,variance,test_size,random_state):
    """
    Function to scale, do principal component analysis and split the data in train and test.

    variance: variance explained by pca
    test_size: the size for the test by the split
    """
    scaled_data = scale(data)
    pca = PCA(variance).fit(scaled_data)
    components = pca.transform(scaled_data)
    X_train, X_test, y_train, y_test= train_test_split(components, labels, test_size=test_size, random_state=random_state)
    return X_train,X_test,y_train,y_test