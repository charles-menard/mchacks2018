from saver import Saver
from preprocess_img import Preprocessor


def predict(model_name="number", img):

    pre = Preprocessor()
    #loading the pickle
    sav=Saver()
    model = sav.load("trained_models/", model_name+ "_model")

    #preprocessing of images
    im = pre.processImage("img/" + "testdeux.jpg", 8, 8)

    return model.predict(im)






print(predict())
