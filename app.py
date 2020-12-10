from flask import Flask, redirect, request, url_for, session, render_template, send_from_directory
import os
import random
from photoMemories import getdetails
from photoMemories import checkdetails
from photoMemories import forgetP
from photoMemories import manageU
from photoMemories import manageP
from photoMemories import manageE
from photoMemories import mkfolder
from photoMemories import photodata
from plyer import notification
from datetime import date

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'some secret key'

@app.route("/", methods=["GET", "POST"])
def main_page():
    errors = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = checkdetails(username, password)
        if result == 1:
            return redirect(url_for('second', username1=username, password1=password))
        else:
            format(request.form["username"])
            errors += "<p>Wrong username or password.</p>\n".format(request.form["password"])

    return render_template("main.html").format(errors=errors)

@app.route('/change_pw/', methods=["GET", "POST"])
def change_pw():
    errors = ""
    if request.method == "POST":
        email = request.form["email"]
        forget = request.form["forget"]
        password = request.form["password"]
        forgetP(email, forget, password)
    return render_template("change_pw.html").format(errors=errors)

@app.route('/create/', methods=["GET", "POST"])
def create():
    errors = ""
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["username"]
        password = request.form["password"]
        forget = request.form["forget"]
        getdetails(email, name, password, forget)
        mkfolder(name)

    return render_template("create.html").format(errors=errors)

#logged in portion of website

@app.route('/second/<username1>/<password1>')
def second(username1, password1):
    session['1'] = username1
    session['2'] = password1
    pics = os.listdir("static/userstorage/" + username1)
    phots = []
    for i in pics:
        if ".txt" in i:
            continue
        else:
            phots.append("userstorage/" + username1 + "/" + i)

    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    print (d1)
    f = open("static/userstorage/" + username1 + "/" + username1 + ".txt")
    info = f.read()
    info = info.split()
    f.close()
    if str(d1) in info:
        notification.notify(title='PhotoMemories', message='You have some memories', app_icon=None, timeout=10,)
    else:
        notification.notify(title='PhotoMemories', message='You have no memories from today', app_icon=None, timeout=10,)
  
    return render_template("second.html", pics = phots).format(username1=username1)



@app.route('/newU/', methods=["GET", "POST"])
def newU():
    errors = ""
    username1 = session['1']
    password1 = session['2']
    if request.method == "POST":
        name = request.form["New Username"]
        manageU(name, password1)
        notification.notify(title='ACCOUNT UPDATE', message='You have changed your username', app_icon=None, timeout=10,)
        return redirect(url_for('main_page'))

    return render_template("newu.html").format(errors=errors, username1=username1)


@app.route('/newP/', methods=["GET", "POST"])
def newP():
    errors = ""
    username1 = session['1']
    if request.method == "POST":
        password = request.form["New Password"]
        manageP(username1, password)
        return redirect(url_for('main_page'))

    return render_template("newp.html").format(errors=errors, username1=username1)

@app.route('/newE/', methods=["GET", "POST"])
def newE():
    errors = ""
    username1 = session['1']
    if request.method == "POST":
        email = request.form["New Email"]
        manageE(username1, email)
        return redirect(url_for('main_page'))

    return render_template("newe.html").format(errors=errors, username1=username1)


@app.route('/upload/', methods=["GET", "POST"])
def upload():
    errors = ""
    username = session['1']
    password = session['2']
    app.config["IMAGE_UPLOADS"] = "static/userstorage/" + username
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            notification.notify(title='ACCOUNT UPDATE', message='You have uploaded an image', app_icon=None, timeout=10,)
            date = request.form["date"]
            cap = request.form["cap"]
            minute = request.form["minute"]
            photodata(username, date, cap, image.filename)
            return redirect(url_for('second', username1=username, password1=password))
            
    return render_template("upload.html").format(errors=errors)

@app.route('/info/', methods=["GET", "POST"])
def info():
    errors = ""
    return render_template("info.html").format(errors=errors)


@app.route('/aboutus/', methods=["GET", "POST"])
def aboutus():
    errors = ""
    return render_template("aboutus.html").format(errors=errors)
