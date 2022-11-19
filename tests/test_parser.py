import unittest
from app.utils.parser import RequestParser

class RequestParserTestCase(unittest.TestCase):
    def test_parser(self) -> None:
        self.assertEqual(
            RequestParser.execute('Пупкин Василий Васильевич'),
            {
                'surname': 'Пупкин',
                'first_name': 'Василий',
                'last_name': 'Васильевич'
            }
        )