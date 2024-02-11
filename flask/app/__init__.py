from flask.app import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_route():
    return "Hello world!"
