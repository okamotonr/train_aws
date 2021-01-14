from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def get():
	return render_template('index.html', \
		title = 'Form Sample(get)', \
		message = 'input your name')

@app.route('/', methods=['POST'])
def post():
	name = request.form['name']
	return render_template('index.html', \
		title = 'Form Sample(post)', \
		message = 'hello, {}'.format(name))
