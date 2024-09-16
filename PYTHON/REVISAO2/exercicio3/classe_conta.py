class Conta_Bancaria():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return f'Olá {self.__titular}, o seu saldo atual é de R${self.__saldo}'
    
    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self.__saldo = valor
        else:
            print("Valor invalido para Saldo")
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else: 
            print("Valor inválido")
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Valor inválido")
            
