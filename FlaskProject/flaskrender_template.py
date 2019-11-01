from flask import Flask, render_template,request,redirect,url_for

# from jinja2 import  Template


app=Flask(__name__)
#
# @app.route("/profile/<name>")
# def profile(name):
#     return render_template("profile.html",name=name)



@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template('users.html',user=user)



# @app.route("/shopping")
# def shopping():
#     food=['eba','ewa','Beef']
#     return render_template('shopping.html',food=food)


@app.route("/question/<name>",methods=['GET','POST'])
def question(name):
    if request.method=='POST':
        if request.form['name']=='dele':
            return redirect(url_for('question',name=name))

    return render_template('users.html')


if __name__=="__main__":
    app.run()
