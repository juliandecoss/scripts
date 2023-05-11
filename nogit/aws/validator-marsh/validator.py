from marshmallow import Schema, fields


class AuthenticationSchema(Schema):
    client_id = fields.String(required=True)
    credential = fields.String(required=True)
    identity = fields.String(required=True)
