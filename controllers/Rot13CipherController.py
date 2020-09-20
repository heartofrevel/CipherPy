from flask import request, Blueprint
from marshmallow import ValidationError

from ciphers.Rot13Cipher import Rot13Cipher
from models.ResultModels import CryptoResult, ErrorResult
from schemas.CipherInputSchema import Rot13Schema

rot13 = Blueprint('rot13', __name__)


@rot13.route('/rot13/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        schema = Rot13Schema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_pt = data.get('input')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = Rot13Cipher(preserve_spaces)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@rot13.route('/rot13/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        schema = Rot13Schema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_ct = data.get('input')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = Rot13Cipher(preserve_spaces)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400
