from unittest import TestCase

import owl.request


class TestRequest(TestCase):

    def test_request_can_be_constructed_using_correct_args(self):
        self.ExampleRequest(a='foo', b='bar')
        # no checks needed here.

    def test_request_throws_request_error_with_invalid_type(self):
        self.assertRaises(
            owl.request.RequestException,
            lambda: self.ExampleRequest({'a': 'foo', 'b': 5})
        )

    def test_request_throws_request_error_with_invalid_value(self):
        self.assertRaises(
            owl.request.RequestException,
            lambda: self.ExampleRequest({'a': 'foo', 'b': 'blah'})
        )

    def test_correct_values_are_stored_in_request(self):
        request = self.ExampleRequest({'a': 'foo', 'b': 'bar'})
        self.assertEqual('foo', request.test_field_1)
        self.assertEqual('bar', request.test_field_2)

    def test_extra_values_cause_request_error_to_be_raised(self):
        self.assertRaises(
            owl.request.RequestException,
            lambda: self.ExampleRequest({'a': 'foo', 'b': 'bar', 'c': 'blah'})
        )

    def test_values_are_modified_as_expected(self):
        class CapitalizingRequest(owl.request.Request):
            test_field = owl.request.Request.Field(
                t=str, modifier=lambda s: s.upper())

            def unpack(self, request_args: 'owl.request.RequestArguments'):
                self.test_field = request_args.get('a')

        request = CapitalizingRequest({'a': 'foo'})
        self.assertEqual('FOO', request.test_field)

    class ExampleRequest(owl.request.Request):
        test_field_1 = owl.request.Request.Field(t=str, valid=('foo', 'bar'))
        test_field_2 = owl.request.Request.Field(t=str, valid=('foo', 'bar'))

        def unpack(self, request_args: owl.request.RequestArguments):
            self.test_field_1: str = request_args['a']
            self.test_field_2: str = request_args['b']


class TestRequestField(TestCase):
    def test_field_with_no_valid_field_arg_passed_accepts_all_values(self):
        field = owl.request.Request.Field(t=int)
        self.assertEqual([], field.validate(2))  # Check no issue is returned.

    def test_field_with_valid_field_arg_passed_accepts_valid_values(self):
        field = owl.request.Request.Field(t=int, valid=(2,))
        self.assertEqual([], field.validate(2))  # Check no issue is returned.

    def test_field_returns_issue_when_invalid_value_passed(self):
        field = owl.request.Request.Field(t=int, valid=(2,))
        self.assertEqual(1, len(field.validate(3)))

    def test_custom_validator_can_add_issue_successfully(self):
        def must_exceed_5(x):
            if x > 5:
                return []
            else:
                return ['Value was not greater than 5']

        field = owl.request.Request.Field(t=int, validator=must_exceed_5)
        self.assertEqual(1, len(field.validate(4)))
