from flask import Blueprint, Flask, render_template, redirect, url_for, request
import json
#from . import db

#auth = Blueprint('auth', __name__)
app = Flask(__name__, static_folder='static')

@app.route('/login')
def login():
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
            print("Congrats you logged in")
            login = True
    if login is False:
        return redirect(url_for('login'))
    
#    return redirect(url_fir(''))

host = '0.0.0.0'

if __name__ == '__main__':
    app.run(host, port=8081)