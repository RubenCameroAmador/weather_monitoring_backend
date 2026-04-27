from marshmallow import Schema, fields

class MeasurementSchema(Schema):
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)
    device_id = fields.String()