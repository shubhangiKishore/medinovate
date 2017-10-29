from flask import Flask
from flask import request
from PIL import Image
import imagehash
import os
from flask import render_template

app = Flask(__name__)
UPLOAD_FOLDER = '/home/sk/Documents/innovacer'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_t():
    file = request.files['imagefile']
    if file:
        file_name = "c"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return 'OK'


'''
def upload_file():
    img_f = Flask.request.files.get('imagefile')
    return hash_it(img_f)
'''





@app.route('/')
def index():
    return render_template('display.html')


@app.route('/hello', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        upload_t()

    hash = imagehash.average_hash(Image.open("c"))
    return str(hash)




if __name__ == "__main__":
    app.run()