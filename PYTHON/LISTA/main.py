from triangulo import Triangulos
from funcaomatematica import matematica
from dados_ex3 import Dados


def main():
    print("ESCOLHA UMA OPÇÃO")
    print("EXERCICIO 1")
    print("EXERCICIO 2")
    print("EXERCICIO 3")
    print("EXERCICIO 4\n")

    opcao = int(input())

    if opcao == 1:
        triangulo = Triangulos()
        print("INNFORME O TAMANHO DOS LADOS DO TRIANGULO")
        a = int(input())
        b = int(input())
        c = int(input())
        print(triangulo.qual_triangulo(a,b,c))
    elif opcao == 2:
        print("INFORME QUAL FUNÇÃO VC QUER UTILIZAR")
        print("1- SENO")
        print("2- COSSENO")
        print("3- TANGENTE")
        print("4- FATORIAL")
        print("5- RAIZ")
        print("6- EXPONENCIAL")
        print("7- POTENCIAL")
        calc = matematica(8, 2)
        print(calc.potencia())

    


if __name__ == "__main__":
    main()



def Ex3():

    saldo = 0

    while True:
        print('1. Visualizar Saldo\n2. Depositar\n3. Sacar\n4. Sair')
        opcao = input('Digite uma opção: ')
        print()
        saldo_cont = Dados.saldo(0, saldo)
        if opcao == '1':
            print(f'R$: {float(saldo_cont):.2f} \n')
        elif opcao == '2':
            val_dep = input('Digite a quantia que será depositada\nR$:  ')
            print()
            saldo = saldo + float(val_dep)
        elif opcao == '3':
            if saldo != 0:
                print(f'R$: {float(saldo_cont):.2f}')
                val_saq = input('Digite o valor que será sacado\nR$: ')
                prev_saldo = saldo - float(val_saq)
                if prev_saldo <= 0:
                    print('Saldo Insuficiente!')
                else:
                    saldo = saldo - float(val_saq)
            else:
                print('Saldo Insuficiente! \n')
        elif opcao == '4':
            break
