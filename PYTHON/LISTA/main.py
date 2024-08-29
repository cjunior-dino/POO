from triangulo import Triangulos
from funcaomatematica import Matematica
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
        a = int(input("INFORME O VERTICE A: "))
        b = int(input("INFORME O VERTICE B: "))
        c = int(input("INFORME O VERTICE C: "))
        print(triangulo.qual_triangulo(a,b,c))
        print(" ")
        main()
    elif opcao == 2:
        print("INFORME QUAL FUNÇÃO VC QUER UTILIZAR")
        print("1- SENO")
        print("2- COSSENO")
        print("3- TANGENTE")
        print("4- FATORIAL")
        print("5- RAIZ")
        print("6- EXPONENCIAL")
        print("7- POTENCIAL")
        
        funcao = int(input())
        
        if funcao == 1:
            a = int(input())
            calc = Matematica()
            print(calc.seno(a)) 
            main()
        elif funcao == 2:
            a = int(input())
            calc = Matematica()
            print(calc.cosseno(a))
            main()
        elif funcao == 3:
            a = int(input())
            calc = Matematica()
            print(calc.tangente(a))
            main()
        elif funcao == 4:
            a = int(input())
            calc = Matematica()
            print(calc.fatorial(a))
            main()
        elif funcao == 5:
            a = int(input())
            calc = Matematica()
            print(calc.raiz(a))
            main()
        elif funcao == 6:
            a = int(input())
            calc = Matematica()
            print(calc.exponencial(a))
            main()
        elif funcao == 7:
            a = int(input())
            calc = Matematica()
            print(calc.potencia(a))
            main()
    elif opcao == 3:
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


if __name__ == "__main__":
    main()



