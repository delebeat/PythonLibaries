from flask import Flask, request,abort

app=Flask(__name__)


# @app.route("/")
# def index():
#     return "Method used: %s" % request.method

# @app.route("/becon",methods=['GET','POST'])
# def becon():
#     if request.method=='POST':
#         return "You are using POST"
#     else:
#         return "You are probably using GET"


# @api.route('/user/<id>')
# def get_user(id):
#     user=load_user(id)



if __name__=="__main__":
    app.run(
    )