from flask import Flask
from flask import Flask, url_for,request,render_template,Markup


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


if __name__=="__main__":
    app.run(debug=True)