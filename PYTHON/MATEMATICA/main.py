class MATEMATICA:
    def  _init_(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):

        return self.numero1 + self.numero2
    
    def quadrado(self):
        return self.numero1 * self.numero1
    
somando = MATEMATICA(2)

print(somando.quadrado())