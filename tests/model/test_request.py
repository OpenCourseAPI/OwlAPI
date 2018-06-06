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

    class ExampleRequest(owl.request.Request):
        test_field_1 = owl.request.Request.Field(t=str, valid=('foo', 'bar'))
        test_field_2 = owl.request.Request.Field(t=str, valid=('foo', 'bar'))

        def unpack(self, request_args: owl.request.RequestArguments):
            self.test_field_1: str = request_args['a']
            self.test_field_2: str = request_args['b']
