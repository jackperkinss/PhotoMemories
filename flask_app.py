from flask import Flask, redirect, request, url_for
#from photoMemories import getdetails
from photoMemories import checkdetails
#from photoMemories import forgotU
#from photoMemories import forgotP
#from photoMemories import manage
#from photoMemories import manageU
#from photoMemories import manageP
#from photoMemories import manageE

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def main_page():
    errors = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = checkdetails(username, password)
        if result == 1:
            return redirect(url_for('second', username=username))
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
                <a href=forgetP>
                    <button>Forgot Password</button>
                </a>
            </body>
        </html>
    '''.format(errors=errors)

@app.route('/second/<username>')
def second(username):
    return '''
        <html>
            <body>
                <p> you are logged in as {username} </p>
                <a href=forgetP>
                    <button>Forgot Password</button>
                </a>
            </body>
        </html>
    '''.format(username=username)

@app.route('/forgetP/')
def forgetP():
    return '''
        <html>
            <body>
                <p>Forgot Password.</p>
            </body>
        </html>
    '''
