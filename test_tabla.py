import unittest
import tablaperiodicav2
from Elemento import elemento1, elemento3

class Tabla_PeriodicaTest(unittest.TestCase):
    def test_basicos(self):
        laTabla = tablaperiodicav2.Tabla_Periodica()
        laTabla.agregar_elemento(elemento1)
        laTabla.agregar_elemento(elemento3)
        self.assertEqual("O", elemento1.simbolo())
        self.assertTrue(laTabla.elementoN(7), elemento3.numeroAtomico())