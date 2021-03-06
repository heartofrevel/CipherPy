from flask import request, Blueprint
from marshmallow import ValidationError

from ciphers.CaesarCipher import CaesarCipher
from models.ResultModels import CryptoResult, ErrorResult
from schemas.CipherInputSchema import CaesarSchema

caesar = Blueprint('caesar', __name__)


@caesar.route('/caesar/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        schema = CaesarSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_pt = data.get('input')
    key = data.get('key')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = CaesarCipher(key, preserve_spaces)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@caesar.route('/caesar/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        schema = CaesarSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_ct = data.get('input')
    key = data.get('key')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = CaesarCipher(key, preserve_spaces)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400
