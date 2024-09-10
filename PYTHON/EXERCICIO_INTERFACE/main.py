import interface
from funcao import Tipo

def usar_interface(obj: interface):
    print(obj.inteiro(1))
    print(obj.flutuante(1.0))
    print(obj.boleano(False))
    print(obj.caractere("True"))

obj = Tipo()
usar_interface(obj)