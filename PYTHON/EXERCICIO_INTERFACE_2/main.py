import interfacefuncao
from classeA import ClasseA
from classeB import ClasseB
from classeC import ClasseC
from classeD import ClasseD

def usar_interface(obj: interfacefuncao):
    print(obj.metodo1())

obj1 = ClasseA()
obj2 = ClasseB()
obj3 = ClasseC()
obj4 = ClasseD()
usar_interface(obj1)
usar_interface(obj2)
usar_interface(obj3)
usar_interface(obj4)