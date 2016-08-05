import tensorflow as tf
import numpy as np
import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import index.html


# Data sets
TRAINING = "data_nace_training.csv"
#TRAINING = "iris_training.csv"
#TEST = "iris_test.csv"
TEST = "data_nace_test.csv"

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
#classifier.fit(x=x_train, y=y_train, steps=200)
classifier.fit(x=x_train, y=y_train, steps=200)


#enter in values
a = []
#for x in xrange(0,8):
#    a.append(raw_input("Enter Data: "))




class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(s):
  		s.send_response(200)
  		s.send_header("Content-type", "text/html")
  		s.end_headers()
  		s.wfile.write(GFW_Tensorflow/index.html)

server_class = BaseHTTPServer.HTTPServer
httpd = server_class(("", 8020), MyHandler)
httpd.serve_forever()


def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

prompts = ["Operational Efficiency: ",
	"Adoption Score: ",
	"Renewal Risk: ",
	"Referencable:",
	"Transformation Agenda: ",
	"Transformation Senior Sponsorship: ",
	"Transformation Senior Relationships: ",
	"Transformation Senior Partner Services: ",
	"Transformation Senior Health Status: "
	]

while len(a) < 8:
	# val = raw_input("Enter Operational Efficiency: ")
	# val = raw_input("Enter Adoption Score: ")
	# val = raw_input("Enter Renewal Risk: ")
	# val = raw_input("Enter Referenceable: ")
	# val = raw_input("Transformation Agenda: ")
	# val = raw_input("Transformation Senior Sponsorship: ")
	# val = raw_input("Transformation Senior Relationships: ")
	# val = raw_input("Transformation Senior Partner Services: ")
	# val = raw_input("Transformation Senior Health Status: ")

	val = raw_input(prompts[len(a)])

	if not val:
		continue
	if not is_int(val) or (int(val) < -2 or int(val) > 1):
		print 'Please enter an integer value between -2 and 1'
		continue
	a.append(int(val))





# Classify two new flower samples.
new_samples = np.array(
    [ a ], dtype=float)
y = classifier.predict(new_samples)
print ('Health Status: {}'.format(str(y)))



# Evaluate accuracy.
#accuracy_score = classifier.evaluate(x=x_test, y=y_test)["accuracy"]
#print('Accuracy: {0:f}'.format(accuracy_score)) 