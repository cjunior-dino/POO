class Pessoa():
    def __init__(self,nome,cpf,data_nasc):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc

class Endereco():
    def __init__(self, bairro, rua, numero, cep):
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.cep = cep

class Empresa(Pessoa, Endereco):
    def __init__(self, nome, cpf, data_nasc, bairro, rua, numero, cep, cnpj, nome_fantasia):
        super().__init__(nome, cpf, data_nasc, bairro, rua, numero,cep)
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia

class Cliente(Pessoa, Empresa):
    def __init__(self, nome, cpf, data_nasc, ):
        super().__init__(nome, cpf, data_nasc)