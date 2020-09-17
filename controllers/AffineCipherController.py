from flask import request
from ciphers.AffineCipher import AffineCipher
from models.ResultModels import CryptoResult
from models.ResultModels import ErrorResult
from flask import Blueprint

affine = Blueprint('affine', __name__)


@affine.route('/affine/encrypt', methods=['POST'])
def encrypt():
    if not request.is_json:
        error = ErrorResult("Malformed Request : Request should be in JSON format")
        return error.json(), 400
    data = request.get_json()
    input_pt = data.get('input')
    key1 = data.get('key1')
    key2 = data.get('key2')
    try:
        algo = AffineCipher(key1, key2)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@affine.route('/affine/decrypt', methods=['POST'])
def decrypt():
    if not request.is_json:
        error = ErrorResult("Malformed Request : Request should be in JSON format")
        return error.json(), 400
    data = request.get_json()
    input_ct = data.get('input')
    key1 = data.get('key1')
    key2 = data.get('key2')
    try:
        algo = AffineCipher(key1, key2)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

