from flask import Flask
from flask import render_template,request,redirect


from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myfirstdb.db"
db=SQLAlchemy(app)

class contact_Us(db.Model):
    
    myid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    mytitle = db.Column(db.String(120))
    mymessage = db.Column(db.Text)
with app.app_context():
    db.create_all() 

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contact():
    return render_template("contactus.html")

@app.route("/services")
def services():
    data=contact_Us.query.all()
    return render_template("services.html",mydata=data)

@app.route("/savethisdata",methods =["POST"])
def savethisdata():
    if request.method  =="POST":
        title=request.form.get("title")
        message=request.form.get("msg")
 
        data=contact_Us(mytitle=title,mymessage=message)
        db.session.add(data)
        db.session.commit()
        return redirect("/contactus")  


@app.route("/deletethisdata/<int:myid>",methods=["POST"])
def deletethisdata(myid):
    user=contact_Us.query.get(myid)
    db.session.delete(user)
    db.session.commit()
    return redirect("/services")


@app.route("/updatethisdata/<int:myid>",methods=["POST"])
def updatathisdata(myid):
    update=contact_Us.query.get(myid)
    return render_template("update.html",yourdata=update)


@app.route("/nowupdatethisdata/<int:myid>",methods=["POST"])
def nowupdatethisdata(myid):
    if request.method=="POST":
        title=request.form.get("title")
        message=request.form.get("msg")
        data=contact_Us.query.get(myid)
        data.mytitle = title
        data.mymessage = message
        db.session.commit()

        return redirect("/services")

 
if __name__ =="__main__":
    app.run(debug=True)