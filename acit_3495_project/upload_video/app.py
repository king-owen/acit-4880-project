import os
from flask import Flask, render_template, request
import ftplib
#import paramiko
#from scp import SCPClient
app = Flask(__name__)
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#session = ftplib.FTP('0.0.0.0:2121', 'root', 'password')


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
        session = ftplib.FTP('172.6.0.5', 'root', 'password')
        f = request.files['file']
        #f.save(f.filename)
        print(f.filename)
        f.save(os.path.join(uploads, f.filename))
        file_serve = open("/acit-4880-project/acit_3495_project/upload_video/upload_folder/" + f.filename, "rb")
        session.storbinary(("STOR " + f.filename), file_serve)
        session.quit()

        #ssh.connect('root@172.18.0.3')
        #with SCPClient(ssh.get_transport()) as scp:
        #    scp.put(os.path.join(uploads, f.filename), os.path.join('uploads/', f.filename))
        
        #request.post('172.18.0.2/uploads', files=('/upload_folder/' + f.filename))

        return 'successful upload'


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host)