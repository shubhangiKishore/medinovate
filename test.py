from flask import Flask
from flask import request
import requests
from PIL import Image
import imagehash
import os
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['STATIC_FOLDER'] = 'static'
UPLOAD_FOLDER = '/home/sk/Documents/innovacer'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_t():

    prescription = request.form['prescription']
    #diagnosis = request.form['diagnosis']
    #p_key = request.form['p-key']
    #file = request.files['imagefile']
    if file:
        file_name = "c"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return prescription


'''
def upload_file():
    img_f = Flask.request.files.get('imagefile')
    return hash_it(img_f)
'''





@app.route('/')
def index():
    return render_template('medinnovate/index.html')



@app.route('/add-patient')


def add_pat():
    return render_template('medinnovate/add-patient.html')


@app.route('/submit-record', methods = ['GET','POST'])
def hello():
    #if request.method == 'POST':
    #    upload_t()

    prescription = request.form['prescription']
    diagnosis = request.form['diagnosis']
    id  = request.form['p-key']
    accessible_by = request.form['p-key']
    image_file = request.files['imagefile']
    record_type = 'xray'
    datacenter = 'bangalore'


    payload = {'id': id, 'record_type': 'xray', 'datacenter': 'bangalore', 'image_file': image_file, 'accessible_by': id}

    #r = requests.post("http://httpbin.org/post", data=payload)



    url = "http://52.91.199.207:82/addRecord"
    response = requests.request("POST", url, data=payload)


    print (response)
    return "Details added!"





if __name__ == "__main__":
    app.run()