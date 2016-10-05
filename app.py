from flask import Flask, render_template, request

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
    authMessage = "Login unsuccessful."
    if u == 'username' and p == 'password':
    	authMessage = "Login successful."
    return render_template('authenticate.html', message = authMessage)

if __name__ == "__main__":
    app.debug = True
    app.run()
