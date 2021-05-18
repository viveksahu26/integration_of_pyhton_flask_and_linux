from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask("linuxapp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

db = SQLAlchemy(app)

class linux(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.Text)

    def __init__(self, cmd):
        self.command = cmd

db.create_all()

@app.route("/linux")
def linuxes():
    return render_template("index.html")

@app.route("/commands",methods=['GET'])
def commands():
    data = request.args.get("cmd")
    command1 = linux(data)
    db.session.add(command1)
    db.session.commit()
    return "<pre>" + subprocess.getoutput(data) + "</pre>" 
