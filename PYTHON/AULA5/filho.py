from pai import Pai
from mae import Mae



class Filho(Pai, Mae):
    def __init__(self, nome_filho, nome_pai, sobrenome_pai, nome_mae, sobrenome_mae):
        self.nome_filho = nome_filho
        Pai.__init__(self,nome_pai,sobrenome_pai)
        Mae.__init__(self,nome_mae,sobrenome_mae)

    def informa(self):
        return f'O {self.nome_filho} é filho de {self.exibir_informacoes_pai} e {self.exibir_informacoes_mae}'
