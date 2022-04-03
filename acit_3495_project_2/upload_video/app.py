import os
from flask import Flask, render_template, request, redirect
import ftplib
import mysql.connector
import requests
import json
app = Flask(__name__)

mydb = mysql.connector.connect(
    host='load-mysql',
    #port='3307',
    user='root',
    password='root',
    database='video'
)


uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_folder')
#print(os.path.dirname(os.path.realpath(__file__)))
print(uploads)
def check_login () :
    r = requests.get(url = "http://load-auth:8081/login_check").json()
    print(r)
    if r['username'] == None:
        return False
    else:
        return True

@app.route('/')
def hello_world():
    if check_login() != True:
        return redirect("http://load-auth:8081/login")
    return 'Hello, World!'

@app.route('/upload')
def upload_files():
    if check_login() != True:
        return redirect("http://load-auth:8081/login")
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if check_login() != True:
        return redirect("http://load-auth:8081/login")
    if request.method == 'POST':
        session = ftplib.FTP('load-ftp', 'root', 'password')
        f = request.files['file']
        #f.save(f.filename)
        print(f)
        f.save(os.path.join(uploads, f.filename))
        file_serve = open("/acit-4880-project/acit_3495_project_2/upload_video/upload_folder/" + f.filename, "rb")
        session.storbinary(("STOR " + f.filename), 
        file_serve)
        session.quit()
        mycursor = mydb.cursor()
        val = (f.filename, "/acit-4880-project/acit_3495_project_2/file_system/uploads/")
        mycursor.execute("INSERT INTO videos (name, path) VALUES (%s, %s)", val)
        mydb.commit()

        return 'successful upload'


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host)