import flask
from controllers.MASCController import masc
from controllers.CaesarCipherController import caesar
from controllers.AffineCipherController import affine

app = flask.Flask(__name__)
app.register_blueprint(masc)
app.register_blueprint(caesar)
app.register_blueprint(affine)


@app.route('/', methods=['GET'])
def main():
    return "Cipher API"


app.run()
