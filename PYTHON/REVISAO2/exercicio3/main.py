from classe_conta import Conta_Bancaria


def main():
    conta = Conta_Bancaria("Carlos", 1000)
    print(conta.saldo)

    conta.depositar(200)

    print(conta.saldo)

    conta.sacar(100)

    print(conta.saldo)

if __name__ == "__main__":
    main()