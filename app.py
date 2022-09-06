from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import url_for

app = Flask(__name__)

@app.route("/mypage/me")
def mypage():
    return render_template('me.html')


@app.route("/mypage/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for("user", usr=user))
    else:
        return render_template("contact.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"        

