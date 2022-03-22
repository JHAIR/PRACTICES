import unittest
from src.calculator import  Calculator


class CalculatorTest (unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)


    def test_age(self):
        cal = Calculator()
        result = cal.age(5)
        self.assertTrue(result, 'result')

    def test_max(self):
        cal = Calculator()
        result = cal.max(9, 8, 6)
        self.assertEqual(8, result)

    def test_numero(self):
        cal = Calculator()
        result = cal.numero('6')
        self.assertTrue(result, 'Es Numero')


    def test_vocal(self):
        cal = Calculator()
        result = cal.vocal('i')
        self.assertTrue(result, 'es vocal')


    def test_letra(self):
        cal = Calculator()
        result = cal.letra('P')
        self.assertFalse(result, 'es letra')


    def test_palindromo(self):
        cal = Calculator()
        result = cal.invertir('ana')
        self.assertEqual('ana',result)


    def test_maxcadena(self):
        cal = Calculator()
        var = ['Portugal', 'Bolivia', 'Argentina', 'Estados Unidos']
        result = cal.maxcadena(var)
        self.assertEqual('Estados Unidos', result)