from unittest import TestCase

import owl.input


class TestInput(TestCase):
    def test_get_one_allows_proper_input(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_get_one_raises_issues_when_extra_arguments_are_received(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'blah': 5,
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertTrue(inputs.errors)

    def test_get_one_disallows_input_without_department(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'course': '1A',
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertEqual(1, len(inputs.errors))

    def test_filter_can_accept_status_argument(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'status': {'open': 1, 'waitlist': 1},
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_filter_can_accept_type_argument(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'type': {'hybrid': 1, 'online': 1},
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_filter_can_accept_days_argument(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'days': {'M': 1, 'T': 1, 'Th': 1},
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_filter_can_accept_instructor_argument(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'instructor': {'PlaceholderName': 1},
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_filter_can_accept_all_arguments(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'status': {'open': 1, 'waitlist': 1},
                'type': {'hybrid': 1, 'online': 1},
                'days': {'M': 1, 'T': 1, 'Th': 1},
                'time': {'start': '8:30 AM', 'end': '4:30 PM'},
                'instructor': {'PlaceholderName': 1},
                'conflict_sections': [
                    {
                        'quarter': '000011',
                        'department': 'CS',
                        'course': '1A',
                        'section': '123456',
                    },
                    {
                        'quarter': '000011',
                        'department': 'CS',
                        'course': '2A',
                        'section': '654321',
                    }
                ]
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_filter_does_not_accept_extra_arguments(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'CS',
            'course': '1A',
            'filter': {
                'foo': {'Placeholder': 1},
            }
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertTrue(inputs.errors)

    def test_get_many_allows_proper_input(self):
        request = PseudoRequest({
            'courses': [
                {
                    'quarter': '000011',
                    'department': 'CS',
                    'course': '1A',
                },
                {
                    'quarter': '000012',
                    'department': 'CS',
                },
                {
                    'quarter': '000011',
                    'department': 'MATH',
                }
            ]
        })
        inputs = owl.input.GetManyInput(request)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_get_many_raises_issues_when_extra_arguments_are_received(self):
        request = PseudoRequest({
            'courses': [
                {
                    'quarter': '000011',
                    'department': 'CS',
                    'course': '1A',
                },
                {
                    'quarter': '000012',
                    'department': 'CS',
                },
                {
                    'quarter': '000011',
                    'department': 'MATH',
                }
            ],
            'unneeded_arg': 2
        })
        inputs = owl.input.GetManyInput(request)
        inputs.validate()
        self.assertTrue(inputs.errors)

    def test_get_list_accepts_expected_arguments(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'MATH',
            'course': '1A',
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_get_list_does_not_accept_unexpected_arguments(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'department': 'MATH',
            'course': '1A',
            'unexpected': 4
        })
        inputs = owl.input.GetOneInput(raw)
        inputs.validate()
        self.assertTrue(inputs.errors)

    def test_get_urls_accepts_valid_input(self):
        raw = PseudoRequest({
            'quarter': '000011',
        })
        inputs = owl.input.GetUrlsInput(raw)
        inputs.validate()
        self.assertFalse(inputs.errors)

    def test_get_urls_does_not_accept_extra_arguments(self):
        raw = PseudoRequest({
            'quarter': '000011',
            'Unneeded': 'CS',
        })
        inputs = owl.input.GetUrlsInput(raw)
        inputs.validate()
        self.assertTrue(inputs.errors)


class PseudoRequest:
    def __init__(self, args):
        self.json = args
