from flask import render_template, Flask
import building

app = Flask(__name__)


def helloworld():
	return 'hello world'


@app.route('/')
def index():
	text = helloworld()
	moretext = building.outronome()
	return render_template('index.html', text=text, moretext=moretext)
