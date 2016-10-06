from flask import Flask, render_template, request
from utils import auth

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def main():
    #print request.headers
    return render_template('login.html')

@app.route("/authenticate", methods = ['POST'])
def auth():
    #print request.headers
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
  	return auth.auth(u, p ,a)

if __name__ == "__main__":
    app.debug = True
    app.run()
