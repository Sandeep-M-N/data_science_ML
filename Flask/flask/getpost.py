from flask import Flask,render_template,request
'''
It creates an instance of the flask class
which will be your WSGI (Web Server Gateway Interface) application
'''
### WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "This is the simple flask application"

## for creating a template in html create a templates folder first and import render_template
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form",methods=["GET","POST"])
def form_data():
    if request.method=="POST":
        name=request.form['name']
        age=request.form['age']
        return f"hello {name} and your age is {age}"
    return render_template("form.html")


if __name__=="__main__":
    app.run(debug=True)
## when debug is not true everytime we make changes in the application we need to restart the server.

