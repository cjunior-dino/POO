class Fogo:
    def __init__(self, nome):
        self.nome = nome

    def lança_chamas(self):
        return f'{self.nome} esta usando o Lança Chamas'

class Grama: 
    def __init__(self, nome):
        self.nome = nome

    def folhas_navalhas(self):
        return f'{self.nome} esta usando o Folhas Navalhas'
class Dragao:
    def __init__(self,nome):
        self.nome = nome

    def meteoro_do_dragao(self):
        return f'{self.nome} esta usando o Meteoro do Dragao'
    
class Voador:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        return f'{self.nome} esta usando o voar'
    
class Pokemon(Fogo, Grama, Dragao, Voador):
    def __init__(self, nome):
        Fogo.__init__(self,nome)
        Grama.__init__(self,nome)
        Dragao.__init__(self,nome)
        Voador.__init__(self,nome)

bubassauro = Pokemon("Bubassaura")
dragonite = Pokemon("Dragonite")

print(bubassauro.folhas_navalhas())
print(dragonite.lança_chamas())
print(dragonite.voar())
print(bubassauro.voar())