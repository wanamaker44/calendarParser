from flask import Flask, escape, request, send_from_directory


app = Flask(__name__)

@app.route('/<file>')
def index(file):
	return send_from_directory('website', file)

@app.route('/sendpayload', methods = ['POST'])
def hello():
	print('returning ', request.data)
	return request.data;