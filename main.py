from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/sevices")
def services():
    return render_template("services.html")
 
if __name__ =="__main__":
    app.run()