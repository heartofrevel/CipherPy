from marshmallow import Schema, fields


class MASCSchema(Schema):
    input = fields.String(required=True)
    key_pt = fields.String(required=True)
    key_ct = fields.String(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class CaesarSchema(Schema):
    input = fields.String(required=True)
    key = fields.Integer(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class AffineSchema(Schema):
    input = fields.String(required=True)
    key1 = fields.Integer(required=True)
    key2 = fields.Integer(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class VigenereSchema(Schema):
    input = fields.String(required=True)
    key = fields.String(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class AtbashSchema(Schema):
    input = fields.String(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class Rot13Schema(Schema):
    input = fields.String(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)


class BeaufortSchema(Schema):
    input = fields.String(required=True)
    key = fields.String(required=True)
    preserve_spaces = fields.Boolean(required=False, missing=False)



