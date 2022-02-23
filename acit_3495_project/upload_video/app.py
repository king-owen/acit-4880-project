import os
from flask import Flask, render_template, request, redirect
import ftplib
import mysql.connector
import requests
import json
#import paramiko
#from scp import SCPClient
app = Flask(__name__)

mydb = mysql.connector.connect(
    host='172.6.0.2',
    user='root',
    password='root',
    database='video'
)
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#session = ftplib.FTP('0.0.0.0:2121', 'root', 'password')


uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_folder')
#print(os.path.dirname(os.path.realpath(__file__)))
print(uploads)
def check_login () :
    r = requests.get(url = "http://172.6.0.6:8081/login_check").json()
    print(r)
    if r['username'] == None:
        return False
    else:
        return True

@app.route('/')
def hello_world():
    if check_login() != True:
        return redirect("http://localhost:8081/login")
    return 'Hello, World!'

@app.route('/upload')
def upload_files():
    if check_login() != True:
        return redirect("http://localhost:8081/login")
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if check_login() != True:
        return redirect("http://localhost:8081/login")
    if request.method == 'POST':
        session = ftplib.FTP('172.6.0.5', 'root', 'password')
        f = request.files['file']
        #f.save(f.filename)
        print(f.filename)
        f.save(os.path.join(uploads, f.filename))
        file_serve = open("/acit-4880-project/acit_3495_project/upload_video/upload_folder/" + f.filename, "rb")
        session.storbinary(("STOR " + f.filename), file_serve)
        session.quit()
        mycursor = mydb.cursor()
        val = (f.filename, "/acit-4880-project/acit_3495_project/file_system/uploads/")
        mycursor.execute("INSERT INTO videos (name, path) VALUES (%s, %s)", val)
        mydb.commit()

        #ssh.connect('root@172.18.0.3')
        #with SCPClient(ssh.get_transport()) as scp:
        #    scp.put(os.path.join(uploads, f.filename), os.path.join('uploads/', f.filename))
        
        #request.post('172.18.0.2/uploads', files=('/upload_folder/' + f.filename))

        return 'successful upload'


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host)