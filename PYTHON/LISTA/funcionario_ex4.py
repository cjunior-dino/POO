from pessoa_ex4 import Pessoa


class Funcionario(Pessoa):
    def __init__(self, id, salario, nome, idade):
        self.id = id
        self.salario = salario
        super().__init__(nome, idade)

    def informacao(self):
        return f'Id: {self.id}\nSalario: {self.salario}\n{super().dados()}'
