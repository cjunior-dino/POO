class Dados_Banco:
    def _init_(self, n_conta, agencia, banco ):
        self.n_conta = n_conta
        self.agencia = agencia
        self.banco = banco

    def _str_(self):
        return  (f"Número da Conta: {self.n_conta}\n"
                 f"Agência: {self.agencia}\n"
                 f"Banco: {self.banco}")

class Titular:
    def _init_(self, nome, cpf_cnpj):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj

    def _str_(self):
        return (f"Conta Corrente:\n"
                f"Nome: {self.nome}\n"
                f"CPF/CNPJ: {self.cpf_cnpj}")