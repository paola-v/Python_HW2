import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwnerForm
from config import username, password, key
app = Flask(__name__)
app.config['SECRET_KEY'] = key

############################
####    SQL DATABASE    ####

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{password}@localhost/dogs_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
Migrate(app,db)


################################
####    DATABASE MODELS     ####

#### CREATE THE DOG MODEL
class Dog(db.Model):

# Manual table name
    __tablename__='dogs'

# Table Column Names
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    breed = db.Column(db.Text)
    color = db.Column(db.Text)
    age = db.Column(db.Integer)
    mood = db.Column(db.Text)
    sex = db.Column(db.Text)     

    # ONE DOG TO ONE OWNER
    owner = db.relationship('Owner',backref='dog',uselist=False)


# Define init and repr method for the class

    def __init__(self,name,breed,color,age,mood,sex):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.mood = mood
        self.sex = sex
        

    def __repr__ (self):
        if self.owner:
            return f"{self.name} is a {self.breed} and it is a good {self.sex}! {self.name}'s owner is {self.owner.name}."
        else:
            return f"{self.name} is a {self.breed} and it is a good {self.sex}! {self.name} does not have an owner yet."
    

#### CREATE THE OWNER MODEL 
class Owner(db.Model):

 # Manual table name   
    __tablename__ = 'owners'

# Table Column Names
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    dog_id = db.Column(db.Integer,db.ForeignKey('dogs.id'))

    def __init__ (self,name,phone, email, dog_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.dog_id = dog_id

    def __repr__(self):
        return f"Owner Name: {self.name}"




######################################
#### VIEW FUNCTIONS -- HAVE FORMS ####

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_owner',methods=['GET','POST'])
def add_owner():
    form = AddOwnerForm()
    
    if form.validate_on_submit():
        name = form.name.data
        dog_id = form.dog_id.data

        new_owner = Owner(name, dog_id)
        db.session.add(new_owner)
        db.session.commit() 

        return redirect(url_for('list_dog'))
    return render_template('add_owner.html',form=form)


@app.route('/add',methods=['GET','POST'])
def add_dog():
    form = AddForm()
    
    if form.validate_on_submit():
        name=form.name.data
        breed=form.breed.data
        color=form.color.data
        age=form.age.data
        mood=form.mood.data
        sex=form.sex.data
        new_dog=Dog(name,breed,age,sex)
        db.session.add(new_dog)
        db.session.commit()

    
        return redirect(url_for('list_dog'))
    return render_template('add.html',form=form)

@app.route('/list')
def list_dog():
    dogs=Dog.query.all()
    return  render_template('list.html',dogs=dogs)

@app.route('/delete',methods=['GET','POST'])
def del_dog():
    form=DelForm()
    if form.validate_on_submit():
        id=form.id.data
        dog=Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        
        return redirect(url_for('list_dog'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)