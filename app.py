from flask import Flask, render_template, request, url_for, redirect, session
from utils import authenticate

app = Flask(__name__)
app.secret_key = "nine"

@app.route("/")
def root():
	if 'user' in session:
		username = session['user']
		return redirect(url_for('auth'))
	else: 
		return redirect(url_for('login'))


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/authenticate", methods = ['POST'])
def auth():
	##if 'user' in session:
		##return render_template('authenticate.html', messageAuthY = "Successfully logged in!", messageAuthI = "you have been in")
	else:
		return authenticate.task(request.form['username'], request.form['password'], request.form['action'])


@app.route("/logout", methods = ['POST'])
def logout():
	session.pop('user')
	redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run()
