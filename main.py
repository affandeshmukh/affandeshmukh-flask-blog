from flask import Flask, render_template,request,session,redirect,g,url_for
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
with open("config.json", "r") as c:
    params = json.load(c)['params']
app = Flask(__name__)
app.secret_key = 'batman dead'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/blogs'
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    phone_num  = db.Column(db.String(12),  nullable=False)
    mess = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(12),  nullable=True)
    email = db.Column(db.String(80),   nullable=False)

   
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    slug  = db.Column(db.String(21),  nullable=False)
    content = db.Column(db.String(120),  nullable=False)
    tagline = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(12),  nullable=True)
  
@app.route("/loretwefxubdifbfifbdclwsbwspwhepodg")
def board():
    
 
            return render_template('logout.html')




@app.route("/")
def index():
    post=Posts.query.filter().all()
    return render_template('index.html', post=post)




@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        ''' Add entry  to the database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry= Contact(name=name, phone_num=phone, mess=message, date=datetime.now() ,email=email)
        db.session.add(entry)
        db.session.commit()
      
    return render_template('contact.html')

@app.route("/post/<string:post_slug>", methods=['GET'])
def posts(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post)

app.run(debug=True)