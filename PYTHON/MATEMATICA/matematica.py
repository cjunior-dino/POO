import math
class Matematica:
    def  __init__(self, numero1, numero2=None):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        if self.numero2 is not None:
            return self.numero1 + self.numero2
        else:
            return self.numero1
    
    def quadrado(self):
        return math.sqrt(self.numero1)
    
    def coseno(self):
        return math.cos(self.numero1)
    
    def seno(self):
        return math.sin(self.numero1)
    
    def tangente(sefl):
        return math.tan(sefl.numero1)
    
    def potencia(self):
        if self.numero2 is not None:
            return math.pow(self.numero1, self.numero2)
        else:
            return math.pow(self.numero1,0)
    
    def logaritmo(self):
        return math.log(self.numero1, self.numero2)
    
    def fatorial(self):
        return math.factorial(self.numero1)
    
    def exponencial(self):
        return math.exp(self.numero1)
