from interface import Interface_Tipos

class Tipo(Interface_Tipos):

    def inteiro(self, variavel):
        if type(int(variavel)):
            return f"{variavel} é do tipo Inteiro"
        else:
            return f"{variavel} não é Inteiro"
    
    def flutuante(self, variavel):
        if type(float(variavel)):
            return f"{variavel} é do tipo Flutuante"
        else:
            return f"{variavel} não é Flutuante"

    def boleano(self, variavel):
        if type(bool(variavel)):
            return f"{variavel} é do tipo Booleano" 
        else:
            return f"{variavel} não é Booleano"
    
    def caractere(self, variavel):
        if type(str(variavel)):
            return f"{variavel} é do tipo Caractere"
        else:
            return f"{variavel} não é Caractere"
        
    

