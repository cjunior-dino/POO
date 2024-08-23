from banco import Dados_Banco, Titular

def criar_conta():
    print("BEM VINDO!")
    print("Vamos criar sua conta?\n")

    nome = input("Digite o seu nome: ")
    cpf_cnpj = input(" CPF ou CNPJ: ")
    numero_conta = input("Número da conta: ")
    agencia = input("Digite o número da agência: ")
    banco = input("Digite o nome do banco:")

    print("Conta criada com sucesso!")

    i = input("Deseja verificar seus dados? [S/N]")
    if i == "S" or i == "s":
        return (f"Nome: {nome.upper()}"
                f"CPF: {cpf_cnpj}"
                f"\nNumero da conta: {numero_conta}"
                f"\nAgência: {agencia}"
                f"\nBanco: {banco.upper()}")
    else:
        return main()



def main():
    while True:
        print("Oque deseja?\n")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Saldo")
        print("5. Sair\n")
        escolha = input("Digite sua escolha: \n")

        if escolha == "1":
            print(criar_conta())

        elif escolha == "2":
            conta = float(input("Valor a ser depositado: R$"))
            print(f"R$ {conta:.2} Depositado!")

        elif escolha == "3":
            saque = float(input("Valor a ser sacado: R$"))
            calc = conta - saque
            print(f"R$ {saque:.2} Sacado!",
                  f"R$ {calc:.2} Na sua conta!")

print(main())