import tensorflow as tf
import numpy as np
import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import cgi


from flask import Flask,request, render_template, send_from_directory
app = Flask(__name__,static_url_path='')

classifier = 0

TRAINING = "data_nace_training.csv"
TEST = "data_nace_test.csv"

def initialiseClassifier():
	#when you initialise the server it initialises the classifier with training 
	#hence the classifier is not refreshed everytime there is an incoming request
	#for input data prediction
	global classifier
		# Data sets
	

	# Load datasets.
	#target_dtype, takes the numpy datatype of the dataset's target value.
	training_set = tf.contrib.learn.datasets.base.load_csv(filename=TRAINING, target_dtype=np.int)
	test_set = tf.contrib.learn.datasets.base.load_csv(filename=TEST, target_dtype=np.int)

	x_train, x_test, y_train, y_test = training_set.data, test_set.data, \
	  training_set.target, test_set.target

	#Deep Neural Network Classifier
	# Build 3 layer DNN with 10, 20, 10 units respectively.
	#classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)
	classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10,  20, 10], n_classes=27)

	# Fit model.

	classifier.fit(x=x_train, y=y_train, steps=200)



@app.route('/')
def index():
  return render_template('index.html')


@app.route('/execute/<data>',methods=["POST"])
def my_link(data):
	OEfficiency =  request.form.getlist('OEfficiency')
	AScore =  request.form.getlist('AScore')
	RRisk =  request.form.getlist('RRisk')
	Referencable =  request.form.getlist('Referencable')
	TAgenda =  request.form.getlist('TAgenda')
	SSponsorship =  request.form.getlist('SSponsorship')
	Relationships=  request.form.getlist('Relationships')
	PServices =  request.form.getlist('PServices')
	Referencable =  request.form.getlist('Referencable')

	

	a = [OEfficiency, AScore, RRisk, Referencable, TAgenda, SSponsorship, Relationships, PServices]



  
	new_samples = np.array(
	    [ a ], dtype=float)
	y = classifier.predict(new_samples)

	print ('Health Status: {}'.format(str(y)))

	print y


  #print request.form
	return render_template('index.html', health = y  )
if __name__ == '__main__':

  initialiseClassifier()
  app.run(host='0.0.0.0',debug=True)