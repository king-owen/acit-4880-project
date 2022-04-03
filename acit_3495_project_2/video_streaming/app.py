import os
from flask import Flask, render_template, request, redirect
import ftplib
import mysql.connector
import requests
import json
#import wget
app = Flask(__name__, static_folder='static')

mydb = mysql.connector.connect(
    host='localhost',
    port='3307',
    user='root',
    password='root',
    database='video'
)

#mycursor = mydb.cursor()

#mycursor.execute("SELECT * from videos;")

#results = mycursor.fetchall()

#print(results)


uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_folder')
#print(os.path.dirname(os.path.realpath(__file__)))
#print(uploads)

path = '/acit-4880-project/acit_3495_project/file_system/uploads/'
#path = os.path.join("C:", "Users", "oande", "BCIT Term 4", "ACIT 4880", "Project", "GitHub", "acit_3495_project", "file_system", "uploads")
#filename = 'WIN_20220219_15_42_17_Pro.mp4'
def check_login () :
    r = requests.get(url = "http://localhost/login_check").json()
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

@app.route('/download')
def download_files():
    if check_login() != True:
        return redirect("http://localhost:8081/login")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * from videos;")

    result = mycursor.fetchall()
    videos = request.form.getlist('handles[]')
    videos = result
    print(videos)
    
    return render_template('download.html', videos=videos)

@app.route('/downloader', methods = ['POST'])
def download_file():
    if check_login() != True:
        return redirect("http://localhost:8081/login")
    if request.method == 'POST':
        session = ftplib.FTP('localhost:21', 'root', 'password')
        print(request)
        file = request.form.get('handles[]')
        print(file)
        session.retrbinary("RETR " + file, 
        open(("/acit-4880-project/acit_3495_project/video_streaming/static/" + file), "wb").write)
        session.quit()

    return render_template('downloader.html', filename=file, title=file)


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host, port=5050)