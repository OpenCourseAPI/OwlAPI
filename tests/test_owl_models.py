from unittest import TestCase

from owl_models import classDataSchema

class TestClassDataSchema(TestCase):
    def test_required_fields(self):
        errors = classDataSchema.validate({})
        self.assertGreater(len(errors.keys()), 0)


    def test_start_date_is_validated(self):
        errors = classDataSchema.validate({'start': ''})
        self.assertIn('start', errors)
        errors = classDataSchema.validate({'start': '24/22'})
        self.assertIn('start', errors)


    def test_end_date_is_validated(self):
        errors = classDataSchema.validate({'end': ''})
        self.assertIn('end', errors)
        errors = classDataSchema.validate({'end': '24/22'})
        self.assertIn('end', errors)
