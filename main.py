from flask import Flask
from flask import render_template,request,redirect




from flask_sqlalchemy import SQLAlchemy




app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myfirstdb.db"
db=SQLAlchemy(app)

class contactUs(db.Model):
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Title = db.Column(db.String(120))
    Message = db.Column(db.Text)

with app.app_context():
    db.create_all() 




@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/savethisdata",methods =["post"])
def savethisdata():
    if request.method  =="POST":
        mytitle=request.form.get("title")
        message=request.form.get("msg")
 
        data = contactUs(Title=mytitle,Message=message)
        db.session.add(data)
        db.session.commit()
        return redirect("/contactus")  
        
    return"this is datt savee................"
 
if __name__ =="__main__":
    app.run()