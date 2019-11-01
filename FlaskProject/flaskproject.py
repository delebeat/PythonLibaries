from flask import Flask,url_for
# from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet
from flask import Flask, url_for,request,render_template,Markup
from flask import Markup



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')







#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# app = Flask(__name__)

#
# @app.route('/')
# def hello_world():
#     return '<h1>Hello, World!</h1>'
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# @app.route('/post/<float:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'
#
# with app.test_request_context():
#     url_for('static', filename='style.css')

#
# @app.route('/')
# def index():
#     return 'index'
#
# @app.route('/login')
# def login():
#     return 'login'
#
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))






if __name__=="__main__":
    app.run(debug=True)












#
# key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
# message = b'gAAAAABb-Ak-2e5jVqMjXiNl8NRk5_agpY8xWU95sbN3bDJiwA-V1s1RWmjXyab3ZwYoPO9l5M1ZQNrQ5TbWD0O44GRsiDW0p0xtGLLvUkbNJv2Tj9KGm1R-t8bCtyawnGroUSJatAip9LSVhgICKmwbZrwbg1EcWE80bfmd7wY4oQ3PC1rkh7bLHNq2I9lHSqdLx0lTGDVA'
#
#
# app =Flask(__name__)
#
#
# @app.route('/')
# def index():
#     # return "Method used: %s",request.method
#     f = Fernet(key)
#     return "testing on flask %s"%(f.decrypt(message))
#
# @app.route("/test")
# def test():
#     return "Method used: %s" % request.method
#
#
# @app.route("/bacon",method=['GET','POST'])
# def bacon():
#     if request.method=='POST':
#         return "you are using POST"
#     # else:
#         # return "You are probably POST"



# @app.route("/")
# def index():
#     return "This is the home page"
#
# @app.route('/tuna')
# def tuna():
#     return "<h2 style='color:red;'>delebeat welcome</h2>"
#
# @app.route('/profile/<username>')
# def profile(username):
#     # return "<h1>My name is bamidele %s</h1>" % username
#     return '{}\'profile'.format(username)
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post_id=range(120000)
#     return "<h1>My name is bamidele %s</h1>" % list(post_id)


# @app.route('/user/<path:subpath>')
# def show_post(subpath):
#     return 'Sub %s' % subpath

# @app.route('/login')
# def login():
#     return 'login'
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login',next='/'))
#     print(url_for('profile',username='john Doe'))



# if __name__=="__main__":
#     app.run(debug=True)
