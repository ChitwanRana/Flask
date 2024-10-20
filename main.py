from flask import Flask
from flask import render_template,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')


@app.route('/pass/<int:score>')
def success(score):
     xyz="PASS"
     return render_template('success.html',value=xyz)

@app.route('/fail/<int:score>')
def fail(score):
     xyz="FAIL"
     return render_template('fail.html',value=xyz)


@app.route('/result/<int:marks>')
def result(marks):
     result=""
     if marks<50:
          result="fail"
     else:
          result="pass"
     return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
     total_score=0
     if request.method=="POST":
          maths=float(request.form['Maths'])   # name=Maths in form use name value
          science=float(request.form['Science'])
          C=float(request.form['C'])
          datascience=float(request.form['Datascience'])
          total_score=float((maths+science+C+datascience)/4)

     res=""
     if total_score>=50:
          res='success'
     else:
          res='fail'
     return(redirect(url_for(res,score=total_score)))



if __name__=="__main__":
     app.run(debug=True)