import os
from flask import Flask, render_template, request
import ftplib
import mysql.connector
#import wget
app = Flask(__name__, static_folder='static')

mydb = mysql.connector.connect(
    host='172.6.0.2',
    user='root',
    password='root',
    database='video'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from videos;")

result = mycursor.fetchall()

print(result)


uploads = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_folder')
#print(os.path.dirname(os.path.realpath(__file__)))
print(uploads)

path = '/acit-4880-project/acit_3495_project/file_system/uploads/'
#path = os.path.join("C:", "Users", "oande", "BCIT Term 4", "ACIT 4880", "Project", "GitHub", "acit_3495_project", "file_system", "uploads")
filename = 'WIN_20220219_15_42_17_Pro.mp4'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/download')
def download_files():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * from videos;")

    result = mycursor.fetchall()
    videos = request.form.getlist('handles[]')
    
    return render_template('download.html')

@app.route('/downloader', methods = ['GET', 'POST'])
def download_file():
    if request.method == 'GET':
        session = ftplib.FTP('172.6.0.5', 'root', 'password')
        #session.cwd(path)
        print(session.pwd())
        session.retrbinary("RETR " + filename, 
        open(("/acit-4880-project/acit_3495_project/video_streaming/static/" + filename), "wb").write)
        #os.rename(filename, "/acit-4880-project/acit_3495_project/video_streaming/static/" + filename)
        #f = request.files['file']
        #f.save(f.filename)
        #print(f.filename)
        #f.save(os.path.join(uploads, f.filename))
        #session.storbinary(("STOR "+f.filename), f)
        session.quit()

        #link = 'ftp://os.path.join("C:", "Users", "oande", "BCIT Term 4", "ACIT 4880", "Project", "GitHub", "acit_3495_project", "file_system", "uploads", "Salaries.csv)'
        #wget.download(link)

        #return "Successful download"
    print(os.path.join(path, filename))
    return render_template('downloader.html', filename=filename, title="video")


host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host, port=5050)