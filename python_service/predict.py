from saver import Saver
from preprocess_img import Preprocessor

def predict(model_name="number",image):
    #loading the pickle
    sav=Saver()
    sav.load(model_name+"model")

    #preprocessing of images
    pre = Preprocessor()
    


predict(image)
