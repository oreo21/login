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
    f = request.form['firstname']
    l = request.form['lastname']
    if f == 'Barack' && l == 'Obama':
    return 'ok'#render_template('authenticate.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
