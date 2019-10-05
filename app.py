from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'static files'

@app.route('/sendpayload')
def hello():
	return getHello()


def getHello():
	return 'payload was received. good work idiot'