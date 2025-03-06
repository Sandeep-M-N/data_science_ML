### building url dynamically
## jinja 2 template engine
'''
{{ }} expressions to print the output in html
{%...%} conditions, for loop etc,
{#..#} this is for comment section
'''
from flask import Flask,render_template,request,redirect,url_for
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
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)
@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'Score':score,'result':res}
    return render_template("result1.html",results=exp)

@app.route("/subject-marks",methods=["GET","POST"])
def subjectmarks():
    if request.method=="POST":
        subject1=int(request.form['subject1'])
        subject2=int(request.form['subject2'])
        subject3=int(request.form['subject3'])
        subject4=int(request.form['subject4'])
        
        totalscore=(subject1 + subject2 + subject3 + subject4)
        return redirect(url_for('successres',score=totalscore))
    else:
        return render_template('marks.html')


if __name__=="__main__":
    app.run(debug=True)
## when debug is not true everytime we make changes in the application we need to restart the server.

