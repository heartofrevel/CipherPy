from flask import request, Blueprint
from marshmallow import ValidationError

from ciphers.AffineCipher import AffineCipher
from models.ResultModels import CryptoResult, ErrorResult
from schemas.CipherInputSchema import AffineSchema

affine = Blueprint('affine', __name__)


@affine.route('/affine/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        schema = AffineSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_pt = data.get('input')
    key1 = data.get('key1')
    key2 = data.get('key2')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = AffineCipher(key1, key2, preserve_spaces)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@affine.route('/affine/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        schema = AffineSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_ct = data.get('input')
    key1 = data.get('key1')
    key2 = data.get('key2')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = AffineCipher(key1, key2, preserve_spaces)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

