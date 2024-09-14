def dividir(a,b):
    try: 
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None
    except TypeError:
        print("Erro: Entrada inválida. Certifique-se de que ambos os valores são numeros.")
    else:
        return resultado
    

def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número")

def main():
    print("Calculadora de Divisão")

    numerador = obter_numero("Digite o numerador: ")
    denominador = obter_numero("Digite o denominador: ")

    resultado = dividir(numerador, denominador)

    print(resultado)

    if __name__ == "__name__":
        main()