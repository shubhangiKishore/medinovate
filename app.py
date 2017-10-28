from flask import Flask
import hashlib
from PIL import Image
import imagehash


app = Flask(__name__)


@app.route("/")


@app.route("/upload", methods = ['POST'])
def upload_file():
    imagefile = Flask.request.files.get('imagefile','')
    return hash_it(imagefile)

def hash_it(img_file):
    hash = imagehash.average_hash(Image.open(img_file))
    return hash


if __name__ == "__main__":
    app.run()