## url for and dynamic url
from flask import Flask
from flask import render_template,url_for,redirect
app=Flask(__name__)

@app.route('/')
def welcome():
     return "welcome to flask application "

@app.route('/pass/<int:score>')
def success(score):
     return "you have acheive "+str(score)+" and you are PASS "

@app.route('/fail/<int:score>')
def fail(score):
     return "you have acheive "+str(score)+" and you are FAIL "


@app.route('/result/<int:marks>')
def result(marks):
     result=""
     if marks<50:
          result="fail"
     else:
          result="pass"
     return redirect(url_for(result,score=marks))


if __name__=='__main__':
     app.run(debug=True)