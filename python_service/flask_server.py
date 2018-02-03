from flask import Flask
import os
from url_image_extractor import Extractor
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
    return "Hello World!"


@app.route("/train/<model>/<path:url>")
def predict(model, url):
    return "Hello World!"