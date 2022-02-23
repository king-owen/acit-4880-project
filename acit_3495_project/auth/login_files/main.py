from flask import Blueprint, Flask, render_template, redirect, url_for, request
import json
#from . import db

#auth = Blueprint('auth', __name__)
app = Flask(__name__, static_folder='static')
session = {}
session['username'] = None
@app.route('/login')
def login_():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    f = open('login')
    data = json.load(f)
    login= False
    for i in data:
        key = i['username']
        value = i['password']
        if (password == value and username == key):
            #login = True
            session['username'] = username
            print("login is ", session['username'])
            return redirect('home')
    if login is False:
        return redirect(url_for('login_'))

@app.route('/login_check', methods = ['GET'])
def get_login():
    print(session)
    return session
    
@app.route('/logout', methods = ["GET"])
def logout():
    session['username'] = None
    return redirect(url_for('login_'))

@app.route('/home')
def home():
    print(session['username'])
    if session['username'] != None:
        return render_template('home.html')
    else:
        return render_template('login.html')
host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host, port=8081)