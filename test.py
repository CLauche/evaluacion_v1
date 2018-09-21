import unittest
from Elemento import elemento1, elemento2


class Elemento_Test(unittest.TestCase):
    def test_basicos(self):
        oxigeno = elemento1
        hidrogeno = elemento2
        self.assertEqual(8, oxigeno.numeroAtomico())
        self.assertEqual(8, oxigeno.cantNeutrones())
        self.assertEqual(2, oxigeno.valencia())
        self.assertEqual("O", oxigeno.simbolo())
        self.assertEqual(1, hidrogeno.numeroAtomico())
        self.assertEqual(1, hidrogeno.pesoAtomico())
        self.assertEqual(1, hidrogeno.valencia())
        self.assertEqual("H", hidrogeno.simbolo())