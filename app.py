from flask import Flask, render_template, request
from utils import authenticate

app = Flask(__name__)
app.secret_key = "\xa0\x0e\xbe_\xa9\xdf\x9a\xb0\xb4\xc8|#\xdc\xcdCg`\x8b\xb7\x150\x1d\xdbNM\xce\xb8\xe2\x16\xe6\x95\x92"

@app.route("/")
@app.route("/login")
def login():
    #print request.headers
    #print url_for("login")
    return render_template('login.html')

@app.route("/authenticate", methods = ['POST'])
def auth():
    #print request.headers
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
    return authenticate.task(u, p ,a)

if __name__ == "__main__":
    app.debug = True
    app.run()
