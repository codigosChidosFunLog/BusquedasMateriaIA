# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from abb.ArbolBinarioBusqueda import ArbolBinarioBusqueda

miArbol = ArbolBinarioBusqueda()
ABB = False
with open("json/abb1.json", "r") as read_file:
    data = json.load(read_file)
    ABB = data["abb"]


def cargarArbolDeJSon():
    for x in ABB:
        valor = x["index"]
        miArbol[valor] = valor


if __name__ == '__main__':

    cargarArbolDeJSon()

    #En el segundo parametro de getItem se usa esta nomenclatura
    # 0-ObtenerPorClaveNormal
    # 1-PrimeroProfundidad
    # 2-PrimeroAnchura

    print(miArbol[15, 1])
    print("/////")
    print(miArbol[15, 2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
