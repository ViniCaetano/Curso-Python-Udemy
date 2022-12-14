try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../Módulo'
            )
        )
    )

except:
    raise


import unittest
from calculadora import Soma, Subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(Soma(5,5), 10)

    def test_soma_5_e_10_deve_retornar_15(self):
        self.assertAlmostEqual(Soma(5,10), 15)

    def test_soma_varias_entradas(self):
        x_y_saidas =(
            (10,10,20),
            (5,5,10),
            (1.5,1.5,3.0),
            (-5,5,0),
            (100,100,200),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(Soma(x,y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Soma("11", 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Soma(11, "0")

    def test_subtrai_5_e_5_deve_retornar_0(self):
        self.assertEqual(Subtrai(5,5), 0)

    def test_subtrai_5_e_10_deve_retornar_5_negativo(self):
        self.assertAlmostEqual(Subtrai(5,10), -5)

    def test_subtrai_varias_entradas(self):
        x_y_saidas =(
            (10,10,0),
            (5,3,2),
            (1.5,0.5,1.0),
            (-5,5,-10),
            (100,10,90),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(Subtrai(x,y), saida)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Subtrai("11", 0)

    def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            Subtrai(11, "0")

if __name__ == '__main__':
    unittest.main(verbosity=1)