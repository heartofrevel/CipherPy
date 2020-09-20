import flask
from controllers.MASCController import masc
from controllers.CaesarCipherController import caesar
from controllers.AffineCipherController import affine
from controllers.VigenereCipherController import vigenere
from controllers.AtbashCipherController import atbash

app = flask.Flask(__name__)
app.register_blueprint(masc)
app.register_blueprint(caesar)
app.register_blueprint(affine)
app.register_blueprint(vigenere)
app.register_blueprint(atbash)


@app.route('/', methods=['GET'])
def main():
    return "Cipher API"


app.run()
