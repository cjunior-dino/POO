class Pai:
    def __init__(self, nome_pai, sobrenome_pai):
        self.nome_pai = nome_pai
        self.sobrenome_pai = sobrenome_pai

    def exibir_informacoes_pai(self):
        return f"Pai: {self.nome_pai} {self.sobrenome_pai}"
    
