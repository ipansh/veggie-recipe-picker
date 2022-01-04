from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://lydfygrzidzsgq:48ec6bf345df39a7debc5927744a2eb97c4016c52a63bbc34b565c947505953a@ec2-3-217-216-13.compute-1.amazonaws.com:5432/d4suf8da0tjnm'
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users2"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, id, email):
        self.email = id
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Create our database model
class Recipe(db.Model):
    __tablename__ = "recipe"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(120), unique=True)
    ingredients = db.Column(db.String(255), unique=True)

    def __init__(self, recipe_id, recipe_name, ingredients):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.ingredients = ingredients

    def __repr__(self):
        return '<Recipe %r>' % self.email


@app.route("/")
def home():
    db.create_all()
    return render_template('main.html')

@app.route("/submitinfo", methods = ['POST'])
def submit():   
    message = [item for item in request.form.values()][0]
    my_user = User(3,message)
    my_recipe = Recipe(3,message, 'asparagus, cream, carrot')
    db.session.add(my_recipe)
    db.session.commit()
    return render_template('result.html')

if __name__  == '__main__': 
    app.run(debug=True)