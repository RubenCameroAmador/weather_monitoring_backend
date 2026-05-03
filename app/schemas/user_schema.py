from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(required=True)
    password_hash = fields.String(load_only=True, required=True)