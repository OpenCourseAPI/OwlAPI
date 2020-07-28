from marshmallow import Schema, fields, validate, EXCLUDE

class ClassDataSchema(Schema):
    dept = fields.Str()
    section = fields.Str()
    course = fields.Str()
    CRN = fields.Int()
    desc = fields.Str()
    status = fields.Str()
    start = fields.Str(format="%m/%d/%Y")
    end = fields.Str(format="%m/%d/%Y")
    # start = fields.Date(format="%m/%d/%Y")
    # end = fields.Date(format="%m/%d/%Y")
    units = fields.Float(min=0)
    seats = fields.Int(min=0)
    wait_seats = fields.Int(min=0)
    wait_cap = fields.Int(min=0)

    class Meta:
        ordered = True
        unknown = EXCLUDE

class ClassTimeSchema(Schema):
    days = fields.Str()
    time = fields.Str()
    room = fields.Str()
    instructor = fields.Str()
    campus = fields.Str(validate=validate.OneOf(['FH', 'FC', 'FO', 'DA', 'DO', '']))

    class Meta:
        ordered = True
        unknown = EXCLUDE

class InterimClassDataSchema(ClassDataSchema, ClassTimeSchema):
    pass
