from flask import request
from ciphers.CaesarCipher import CaesarCipher
from models.ResultModels import CryptoResult
from models.ResultModels import ErrorResult
from flask import Blueprint

caesar = Blueprint('caesar', __name__)


@caesar.route('/caesar/encrypt', methods=['POST'])
def encrypt():
    if not request.is_json:
        error = ErrorResult("Malformed Request : Request should be in JSON format")
        return error.json(), 400
    data = request.get_json()
    input_pt = data.get('input')
    key = data.get('key')
    try:
        algo = CaesarCipher(key)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@caesar.route('/caesar/decrypt', methods=['POST'])
def decrypt():
    if not request.is_json:
        error = ErrorResult("Malformed Request : Request should be in JSON format")
        return error.json(), 400
    data = request.get_json()
    input_ct = data.get('input')
    key = data.get('key')
    try:
        algo = CaesarCipher(key)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

