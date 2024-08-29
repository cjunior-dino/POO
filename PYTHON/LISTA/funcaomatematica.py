import math

class Matematica:
    def __init__(self, p1, p2 = None):
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
        if self.p1 <= 0 or self.p2 <= 2:
            return "O logaritmando tem que ser maior ou igual a 1 e a base não pode ser menor ou igual a 1"
        else:
            return math.log(self.p1, self.p2)
