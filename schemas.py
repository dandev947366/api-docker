from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    price = fields.Str(dump_only=True)
    store_id = fields.Str(dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str(dump_only=True)
    price = fields.Float(dump_only=True)


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
