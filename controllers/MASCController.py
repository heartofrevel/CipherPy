from flask import request, Blueprint
from marshmallow import ValidationError

from ciphers.MonoAlphabeticSubstitutionCipher import MonoAlphabeticSubstitutionCipher
from models.ResultModels import CryptoResult, ErrorResult
from schemas.CipherInputSchema import MASCSchema

masc = Blueprint('masc', __name__)


@masc.route('/masc/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json
        schema = MASCSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_pt = data.get('input')
    key_pt = data.get('key_pt')
    key_ct = data.get('key_ct')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = MonoAlphabeticSubstitutionCipher(key_pt, key_ct, preserve_spaces)
        cipher = algo.encrypt(input_pt)
        result = CryptoResult(input_pt, cipher)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400


@masc.route('/masc/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.json
        schema = MASCSchema()
        data = schema.load(data)
    except ValidationError as e:
        error = ErrorResult(e.messages)
        return error.json(), 400
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

    input_ct = data.get('input')
    key_pt = data.get('key_pt')
    key_ct = data.get('key_ct')
    preserve_spaces = data.get('preserve_spaces')
    try:
        algo = MonoAlphabeticSubstitutionCipher(key_pt, key_ct, preserve_spaces)
        plain = algo.decrypt(input_ct)
        result = CryptoResult(plain, input_ct)
        return result.json(), 200
    except Exception as e:
        error = ErrorResult(str(e))
        return error.json(), 400

