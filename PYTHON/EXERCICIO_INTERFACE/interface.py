from abc import ABC, abstractclassmethod

class Interface_Tipos(ABC):
    @abstractclassmethod
    def inteiro(self, variavel):
        pass
    
    @abstractclassmethod
    def flutuante(self, variavel):
        pass

    @abstractclassmethod
    def boleano(self, variavel):
        pass
    
    @abstractclassmethod
    def caractere(self, variavel):
        pass
