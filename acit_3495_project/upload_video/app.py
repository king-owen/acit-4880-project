import os
from flask import Flask, render_template, request
app = Flask(__name__)

uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_folder')
#print(os.path.dirname(os.path.realpath(__file__)))
print(uploads)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload')
def upload_files():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(f.filename)
        #print(f)
        f.save(os.path.join(uploads, f.filename))
        
        return 'successful upload'


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host)