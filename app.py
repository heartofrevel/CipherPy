import flask
from controllers.MASCController import masc
from controllers.CaesarCipherController import caesar
from controllers.AffineCipherController import affine
from controllers.VigenereCipherController import vigenere
from controllers.AtbashCipherController import atbash
from controllers.Rot13CipherController import rot13

app = flask.Flask(__name__, static_url_path='', static_folder='')
app.register_blueprint(masc)
app.register_blueprint(caesar)
app.register_blueprint(affine)
app.register_blueprint(vigenere)
app.register_blueprint(atbash)
app.register_blueprint(rot13)


@app.route('/', methods=['GET'])
def main():
    return app.send_static_file('index.html')


app.run()
