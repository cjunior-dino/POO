class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dados(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'