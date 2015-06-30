from flask import render_template, Flask

app = Flask(__name__)


def helloworld():
	return 'hello world'


@app.route('/')
def index():
	text = helloworld()
	return render_template('index.html', text=text)
