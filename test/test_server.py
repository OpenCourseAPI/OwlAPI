from unittest import TestCase

from server import generate_url


class TestGenerateURL(TestCase):
    def test_sample_url_can_be_generated(self):
        self.assertEqual(
            {'dept': 'test_dept', 'course': 'test_course'},
            generate_url('test_dept', 'test_course')
        )
