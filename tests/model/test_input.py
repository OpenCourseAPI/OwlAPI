from unittest import TestCase, SkipTest

import owl.input


class TestInput(TestCase):
    def test_get_one_allows_proper_input(self):
        raw = NotRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    @SkipTest
    def test_get_one_disallows_input_without_department(self):
        raw = NotRequest({
            'quarter': '000011',
            'course': '1A',
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertEqual(1, len(inputs.errors))

    def test_get_urls_accepts_valid_input(self):
        raw = NotRequest({
            'quarter': '000011',
        })
        inputs = owl.input.GetUrlsInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_get_urls_does_not_accept_extra_arguments(self):
        raw = NotRequest({
            'quarter': '000011',
            'Unneeded': 'CS',
        })
        inputs = owl.input.GetUrlsInput(raw)
        inputs.validate()
        self.assertTrue(inputs.errors)


class NotRequest:
    def __init__(self, args):
        self.json = args
