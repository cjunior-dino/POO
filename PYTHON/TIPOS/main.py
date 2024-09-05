class Inteiro:
    def __init__(self) -> None:
        pass

    def teste(self, tipo):
        if tipo is int:
            return "É um Inteiro"
        

class Ponto_Flutuante:
    def __init__(self) -> None:
        pass
    
    def teste(self, tipo):
        if tipo is float:
            return "É um Ponto_Flutuante"

class Booleano:
    def __init__(self) -> None:
        pass
    
    def teste(self, tipo):
        if tipo is bool:
            return "É um Booleano"

class Caractere:
    def __init__(self) -> None:
        pass

    def teste(self, tipo):
        if tipo is str:
            return "É um Caracter"

class Variavel(Caractere,Ponto_Flutuante,Booleano,Inteiro):
    def __init__(self) -> None:
        super().__init__()

    def teste(self, tipo):
        return super().teste(tipo)
    
print(Variavel.mro())
