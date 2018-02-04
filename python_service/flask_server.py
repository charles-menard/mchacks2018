from flask import Flask
import os
from url_image_extractor import Extractor
from predict import pred
from train import trainModel
from flask import send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload/<string:model>/<string:image_class>/<path:url>')
def show_user_profile(model, image_class, url):
    directory = "./models/" + model + "/" + image_class
    if not os.path.exists(directory):
        os.makedirs(directory)
    extractor = Extractor(directory)
    extractor.extract(url)
    return url

@app.route("/train/<model>")
def train(model):
    trainModel(model, "rdf")
    return "Hello World!"


@app.route("/predict/<model>/<path:url>")
def predict(model, url):
    directory = "./prediction_images/" + model
    if not os.path.exists(directory):
        os.makedirs(directory)
    extractor = Extractor(directory)
    extractor.extract(url, "temp")
    return str(pred(model)[0])


@app.route('/get_image/<model>')
def get_image(model):
    image_name = "accuracy_" + model + "_model.png"
    path = "./trained_models/"
    return send_from_directory(path, image_name, mimetype='image/gif')

app.run(host='0.0.0.0')