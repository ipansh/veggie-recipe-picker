from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, SubmitField

app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://lydfygrzidzsgq:48ec6bf345df39a7debc5927744a2eb97c4016c52a63bbc34b565c947505953a@ec2-3-217-216-13.compute-1.amazonaws.com:5432/d4suf8da0tjnm'
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

class InfoForm(FlaskForm):
    '''
    This general class gets all forms submitted on the main page.
    '''
    user_name = StringField('What is your name?')
    diet = RadioField('What is your diet?', choices=[('pescetarian','pescetarian'),('omnivore','omnivore'),('vegetarian','vegetarian'),('vegan','vegan')])
    ingredients = TextAreaField('What ingedients do you have?')
    submit = SubmitField('Submit')

# Create our database model
class UserPreference(db.Model):
    __tablename__ = "user_preference"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    diet = db.Column(db.String(120), unique=False)
    ingredients = db.Column(db.String(255), unique=False)

    def __init__(self, id, name, diet, ingredients):
        self.id = id
        self.name = name
        self.diet = diet
        self.ingredients = ingredients

    def __repr__(self):
        return '<E-mail %r>' % self.name

"""
# Create our database model
class Recipe2(db.Model):
    __tablename__ = "recipe2"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(120), unique=False)
    ingredients = db.Column(db.String(255), unique=False)

    def __init__(self, recipe_id, recipe_name, ingredients):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.ingredients = ingredients

    def __repr__(self):
        return '<Recipe %r>' % self.email
"""

@app.route("/", methods = ['GET','POST'])
def home():

    db.create_all()

    form = InfoForm()

    if form.validate_on_submit():
        user_name = form.user_name.data
        diet = form.diet.data
        ingredients = form.ingredients.data
        last_id = db.session.query(UserPreference.id).order_by(UserPreference.id.desc()).first()[0]
        new_user_preference = UserPreference(last_id+1, user_name, diet, ingredients)
        db.session.add(new_user_preference)
        db.session.commit()

        return redirect(url_for('submit'))

    return render_template('main.html', form = form)

@app.route("/submitinfo", methods = ['GET','POST'])
def submit():
    return render_template('result.html')

if __name__  == '__main__': 
    app.run(debug=True) 