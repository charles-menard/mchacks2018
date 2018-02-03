from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload/<string:model>/<string:image_class>/<path:url>')
def show_user_profile(model, image_class, url):
    directory = "./" + model + "/" + image_class
    if not os.path.exists(directory):
        os.makedirs(directory)
    return url