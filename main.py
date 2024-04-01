from flask import Flask
from flask import render_template,request




app=Flask(__name__)

@app.route("/")
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

@app.route("/savethisdata",methods =["post"])
def savethisdata():
    if request.method =="POST":
        mytitile=request.form.get("title")
        message=request.form.get("msg")
        print(mytitile,message)
    return"this is datt savee................"
 
if __name__ =="__main__":
    app.run()