from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template1.html')



@app.route('/execute/<data>',methods=["POST"])
def my_link(data):


  print request.form
  return render_template('template1.html')
if __name__ == '__main__':
  app.run(debug=True)