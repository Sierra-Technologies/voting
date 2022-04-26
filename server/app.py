from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy






app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rvedwtshfqhxht:93ea18cfbc24e2e202f38a2a0e2df6438d734d5acb72dddadf39bff77cb3fb31@ec2-3-223-213-207.compute-1.amazonaws.com:5432/dfuf3qqoobefl9'
db = SQLAlchemy(app)

class Nominee(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String())
    category = db.Column(db.String())

    def __init__(self,name,category):
        self.name = name
        self.category = category

class Vote(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    pin = db.Column(db.String())
    status = db.Column(db.String())
    

    def __init__(self,name,category):
        self.name = name
        self.category = category
   

class Vote(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    vcount = db.Column(db.String())
    nominee = db.Column(db.String())

    def __init__(self,name,category):
        self.name = name
        self.category = category
   
@app.route('/')
def hello():
    return "Hello World!!!"

if __name__ == "__main__":
    app.run(debug = True, port=9000)
    