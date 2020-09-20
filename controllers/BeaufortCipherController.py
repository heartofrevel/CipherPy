from flask import request, Blueprint
from marshmallow import ValidationError

from ciphers.BeaufortCipher import BeaufortCipher
from models.ResultModels import CryptoResult, ErrorResult
from schemas.CipherInputSchema import BeaufortSchema

beaufort = Blueprint('beaufort', __name__)


@beaufort.route('/beaufort/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        schema = BeaufortSchema()
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
        algo = BeaufortCipher(key, input_pt, preserve_spaces)
        cipher = algo.encrypt()
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@beaufort.route('/beaufort/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        schema = BeaufortSchema()
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
        algo = BeaufortCipher(key, input_ct, preserve_spaces)
        plain = algo.decrypt()
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400
