import interface
from implementacao import Implementacao

def usar_interface(obj: interface):
    print(obj.metodo1())
    print(obj.metodo2("--- método 2 ---"))
    print(obj.metodo3("--- método 3 ---"))
    print(obj.metodo4("--- método 4 ---"))

obj = Implementacao()
usar_interface(obj)