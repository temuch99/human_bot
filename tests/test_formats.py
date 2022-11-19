import unittest
from app.utils.formats import Number, Fio, Surname

class FormatsTestCase(unittest.TestCase):
    def test_number_formats(self) -> None:
        self.assertFalse(Number.check('+7914123123'))
        self.assertTrue(Number.check('7914123123'))
        self.assertFalse(Number.check('8914123123123'))
        self.assertFalse(Number.check('9123123123'))
        self.assertFalse(Number.check('+89123123'))

    def test_fio_formats(self) -> None:
        self.assertTrue(Fio.check('Василий Васильевич Пупкин'))
        self.assertTrue(Fio.check('Василий   Васильевич  Пупкин'))

    def test_surname_formats(self) -> None:
        self.assertTrue(Surname.check('Василий В.А.'))
        self.assertTrue(Surname.check('Василий  В.А.'))
        self.assertTrue(Surname.check('Василий  А. В.'))