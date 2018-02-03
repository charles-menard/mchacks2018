import random
import urllib.request
import sys
import os


class Extractor:
    def __init__(self, path):
        self.path = path
    
    def extract(self, url, name="random"):
        
        if name == "random":
            name = random.randint(0, sys.maxsize)
            
        name = str(name) + ".jpg"
        
        full_name = os.path.join(self.path, name)
        urllib.request.urlretrieve(url ,full_name)

    

