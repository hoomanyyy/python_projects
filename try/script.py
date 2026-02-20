from flask import *
import time
import mysql.connector
import os

from werkzeug.utils import secure_filename

cnx = mysql.connector.connect(
    user="root", password="Al561089", host="127.0.0.1", database="try"
)


app = Flask(__name__)


upload = os.path.curdir + r'/upload/'
app.config["photo"] = upload

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/pannel", methods=["POST", "GET"])
def pannel():

    cursor = cnx.cursor()
    in_database = cursor.execute("SELECT * FROM try;")
    row = cursor.fetchall()

    name = request.form["name"]
    gmail = request.form["gmail"]
    age = request.form["age"]
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password or not name or not age or not gmail:
        age = str(age)
        return render_template("signup.html", text_raise="you dont complete the form !")

    if (name, gmail, age, username, password) not in row:
        query = f"INSERT INTO try VALUES ('{name}' , '{gmail}' , '{age}' , '{username}' , '{password}');"
        cursor.execute(query)
        cnx.commit()
        return redirect(url_for("waite"))


@app.route("/pleasewaite")
def waite():
    time.sleep(1)
    return render_template("done_signup.html")


@app.route("/log", methods=["GET", "POST"])
def go():
    go_button = request.form.get("go")
    time.sleep(0.3)
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def go_signup():
    go_signup = request.form["go_signup"]
    time.sleep(1)
    return redirect(url_for("signup"))


@app.route("/login", methods=["GET", "POST"])
def go_login():
    button_go_login = request.form["button_login"]
    time.sleep(0.7)
    return redirect(url_for("login"))


@app.route("/loginc", methods=["GET", "POST"])
def loginc():
    username = request.form["user"]
    password = request.form["pass"]

    cursor = cnx.cursor(buffered=True)
    cursor.execute(
        "SELECT * FROM try WHERE username = %s AND password = %s", (username, password)
    )
    in_data = cursor.fetchone()
    cursor.close()

    if in_data:
        return redirect(url_for("dashbord"))
    else:
        return render_template("False.html")


@app.route("/dashbord", methods=["GET" , "POST"])
def dashbord():
    
    username = ""
    
    if request.method == "POST":
        
        cursor = cnx.cursor(buffered=True)
        user = request.form.get("username" , '').strip()
        cursor.execute(
            "SELECT username FROM try WHERE username = %s", (user,)
        )
        data = cursor.fetchone()
        cursor.close()

        button = request.form.get("go" , "").strip()
        
        if button:
            return redirect(url_for("profile"))
                
        if data:
            return render_template("dashbord.html" , username=user)   
        else:
            return render_template("dashbord.html" , username="no search usenrame")
            
    return render_template("dashbord.html")


@app.route("/dashbord/my-profile" , methods=['GET' , 'POST'])
def profile():
    return render_template("profile.html")
    

@app.route("/profile" , methods=["POST" , "GET"])
def pprofile():
    return render_template("pprofile.html")


@app.route("/uploadprofile" , methods=["POST"])
def uploadprofile():
    
    fphoto = request.files["photo"]
    print(fphoto)
    secure = secure_filename(fphoto.filename)     
    fphoto.save(os.path.join(app.config["photo"] , secure))
    return "done you create your profile"
    
            
@app.errorhandler(404)
def error_404(error):
    return render_template("404.html")


@app.route("/routes")
def routes():
    return render_template("routes.html")


if __name__ == "__main__":
    app.run(debug=True)