import math

class matematica:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def seno(self):
        return math.sin(self.p1)

    def cosseno(self):
        return math.cos(self.p1)

    def tangente(self):
        return math.tan(self.p1)

    def fatorial(self):
        return math.factorial(self.p1)

    def raiz(self):
        return math.sqrt(self.p1)

    def exponencial(self):
        return math.exp(self.p1)

    def potencia(self):
        return math.pow(self.p1, self.p2)

    def logaritimo(self):
        return math.log(self.p1)
