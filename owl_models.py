from datetime import datetime
from marshmallow import Schema, fields, validate, validates, ValidationError, EXCLUDE

class ClassDataSchema(Schema):
    """
    Class Strings
    """
    # 5-digit Course Reference Number (ex. 25668)
    CRN = fields.Int(required=True)
    # Raw course string (ex. "MATH F001D.01Z")
    raw_course = fields.Str(required=True)
    # Department (ex. "CIS" or "MATH")
    dept = fields.Str(required=True)
    # Course (ex. "1A" or "31D")
    course = fields.Str(required=True)
    # Class section (ex. "01Z")
    section = fields.Str()
    # Class variant (ex. "Z")
    variant = fields.Str(validate=validate.OneOf(['', 'W', 'Z', 'Y', 'H']))

    """
    Course Info
    """
    # Description
    desc = fields.Str(required=True)
    # Class units
    units = fields.Float(required=True, min=0)

    """
    Class Dates
    """
    # Start date
    start = fields.Str(required=True)
    # End date
    end = fields.Str(required=True)

    """
    Seat info
    """
    # Class status (Open, Waitlist, Full)
    status = fields.Str(required=True, validate=validate.OneOf(['open', 'waitlist', 'full']))
    # Number of open seats
    seats = fields.Int(required=True, min=0)
    # Number of open waitlist seats
    wait_seats = fields.Int(required=True, min=0)
    # Waitlist capacity (total # of waitlist seats)
    wait_cap = fields.Int(required=True, min=0)

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @validates('start')
    @validates('end')
    def validate_date(self, date_str):
        """
        Validate the date string format
        """
        try:
            datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            raise ValidationError('Date must be in the format %m/%d/%Y.')


class ClassTimeSchema(Schema):
    days = fields.Str(required=True)
    time = fields.Str(required=True)
    room = fields.Str(required=True)
    instructor = fields.Str(required=True)
    campus = fields.Str(required=True, validate=validate.OneOf(['FH', 'FC', 'FO', 'DA', 'DO', '']))

    class Meta:
        ordered = True
        unknown = EXCLUDE


class InterimClassDataSchema(ClassDataSchema, ClassTimeSchema):
    pass


classDataSchema = ClassDataSchema()
classTimeSchema = ClassTimeSchema()
interimClassDataSchema = InterimClassDataSchema()
