class Elemento:
    def __init__(self, nombre, numeroAtomico, cantNeutrones, valencia, simbolo):
        self.__nombre = nombre
        self.__numeroAtomico = numeroAtomico
        self.__cantNeutrones = cantNeutrones
        self.__valencia = valencia
        self.__simbolo = simbolo


    def nombre(self):
        return self.__nombre


    def numeroAtomico(self):
        return self.__numeroAtomico

    def cantNeutrones(self):
        return self.__cantNeutrones

    def simbolo(self):
        return self.__simbolo

    def valencia(self):
        return self.__valencia

    def cantElectrones(self):
        return self.__numeroAtomico

    def cantProtones(self):
        return self.__numeroAtomico

    def pesoAtomico(self):
        return self.__numeroAtomico + self.__cantNeutrones


# para cada elemento agregado se ingresa la cantidad de neutrones que posee,/
#  de manera de facilitar el cálculo del pesoAtomico
# orden en el que se ingresan las variables: (numeroAtomico, cantNeutrones, valencia, simbolo)
#definí nombre de manera de poder evitar el error de referencia que me aparecía en los test

elemento1 = Elemento("oxigeno", 8, 8, 2, "O")
elemento2 = Elemento("hidrogeno", 1, 0, 1, "H")
elemento3 = Elemento("nitrogeno",7, 7, 5, "N")

