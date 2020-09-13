import flask
from controllers.MASCController import masc

app = flask.Flask(__name__)
app.register_blueprint(masc)


@app.route('/', methods=['GET'])
def main():
    return "Cipher API"


app.run()
