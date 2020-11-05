from flask import Flask, redirect, request, url_for, session
from photoMemories import getdetails
from photoMemories import checkdetails
from photoMemories import forgetP
from photoMemories import manageU
from photoMemories import manageP
from photoMemories import manageE
from plyer import notification

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

    return '''
        <html>
            <body>
                {errors}
                <p>Username</p>
                <form method="post" action=".">
                    <p><input name="username" /></p>
                <p>Password</p>
                <form method="post" action=".">
                    <p><input name="password" /></p>
                    <p><input type="submit" value="Login" /></p>
                </form>
                <a href=change_pw>
                    <button>Forgot Password</button>
                <br>
                <br>
                </a>
                </form>
                <a href=create>
                    <button>Create A Profile</button>
                </a>
            </body>
        </html>
    '''.format(errors=errors)

@app.route('/change_pw/', methods=["GET", "POST"])
def change_pw():
    errors = ""
    if request.method == "POST":
        email = request.form["email"]
        forget = request.form["forget"]
        password = request.form["password"]
        forgetP(email, forget, password)
    return '''
        <html>
            <body>
            {errors}
                <p>Email</p>
                <form method="post" action=".">
                    <p><input name="email" /></p>
                <p>Lucky Number</p>
                <form method="post" action=".">
                    <p><input name="forget" /></p>
                <p>New Password</p>
                <form method="post" action=".">
                    <p><input name="password" /></p>
                <p><input type="submit" value="Submit" /></p>
                </form>
                <a href=/>
                    <button>Back</button>
                </a>
            </body>
        </html>
    '''.format(errors=errors)

@app.route('/create/', methods=["GET", "POST"])
def create():
    errors = ""
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["username"]
        password = request.form["password"]
        forget = request.form["forget"]
        getdetails(email, name, password, forget)

    return '''
        <html>
            <body>
                {errors}
                <p>Username</p>
                <form method="post" action=".">
                    <p><input name="username" /></p>
                <p>Password</p>
                <form method="post" action=".">
                    <p><input name="password" /></p>
                <p>Email</p>
                <form method="post" action=".">
                    <p><input name="email" /></p>
                <p>Lucky Number</p>
                <form method="post" action=".">
                    <p><input name="forget" /></p>
                    <p><input type="submit" value="create" /></p>
                    </form>
                <a href=/>
                    <button>Back</button>
                </a>
            </body>
        </html>
    '''.format(errors=errors)

""" loged in portion of website"""

@app.route('/second/<username1>/<password1>')
def second(username1, password1):
    session['1'] = username1
    session['2'] = password1
    return '''
        <html>
            <body>
                <p> you are logged in as {username1} </p>
                <a href=/newU/>
                    <button>Change Username</button>
                <br>
                <br>
                <a href=/newP/>
                    <button>Change Password</button>
                <br>
                <br>
                <a href=/newE/>
                    <button>Change Email</button>
                </a>
            </body>
        </html>
    '''.format(username1=username1)


@app.route('/newU/', methods=["GET", "POST"])
def newU():
    errors = ""
    username1 = session['1']
    password1 = session['2']
    if request.method == "POST":
        name = request.form["New Username"]
        manageU(name, password1)
        notification.notify(title='Here is the title', message='Here is the message', app_icon=None, timeout=10,)
        return redirect(url_for('main_page'))

    return'''
        <html>
            <body>
            <p>{username1}, Please Enter A New Username</p>
            <form method="post" action=".">
                    <p><input name="New Username" /></p>
                    <p><input type="submit" value="Submit" /></p>
            </body>
        </html>
     '''.format(errors=errors, username1=username1)


@app.route('/newP/', methods=["GET", "POST"])
def newP():
    errors = ""
    username1 = session['1']
    if request.method == "POST":
        password = request.form["New Password"]
        manageP(username1, password)
        return redirect(url_for('main_page'))

    return'''
        <html>
            <body>
            <p>{username1}, Please Enter A New Password</p>
            <form method="post" action=".">
                    <p><input name="New Password" /></p>
                    <p><input type="submit" value="Submit" /></p>
            </body>
        </html>
     '''.format(errors=errors, username1=username1)

@app.route('/newE/', methods=["GET", "POST"])
def newE():
    errors = ""
    username1 = session['1']
    if request.method == "POST":
        email = request.form["New Email"]
        manageE(username1, email)
        return redirect(url_for('main_page'))

    return'''
        <html>
            <body>
            <p>{username1}, Please Enter A New Email</p>
            <form method="post" action=".">
                    <p><input name="New Email" /></p>
                    <p><input type="submit" value="Submit" /></p>
            </body>
        </html>
     '''.format(errors=errors, username1=username1)

