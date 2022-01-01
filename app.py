from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/submitinfo", methods = ['POST'])
def submit():
    #message = request.form.values()[0]
    return render_template('result.html')

if __name__  == '__main__': 
    app.run(debug=True)