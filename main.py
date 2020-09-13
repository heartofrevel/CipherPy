import flask
from flask import request
from ciphers.MonoAlphabeticSubstitutionCipher import MonoAlphabeticSubstitutionCipher
from models.ResultModels import CryptoResult
from models.ResultModels import ErrorResult

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/masc/encrypt', methods=['POST'])
def masc_encrypt():
    if not request.is_json:
        return "Request is not json"
    data = request.get_json()
    input_pt = data.get('input')
    key_pt = data.get('key_pt')
    key_ct = data.get('key_ct')
    try:
        algo = MonoAlphabeticSubstitutionCipher(key_pt, key_ct)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@app.route('/masc/decrypt', methods=['POST'])
def masc_decrypt():
    if not request.is_json:
        return "Request is not json"
    data = request.get_json()
    input_ct = data.get('input')
    key_pt = data.get('key_pt')
    key_ct = data.get('key_ct')
    try:
        algo = MonoAlphabeticSubstitutionCipher(key_pt, key_ct)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


app.run()
