class Pessoa():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def apresenta(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é {self.email}"

def main():    
    pessoa1 = Pessoa("Carlos", 25, "cmbj.dev@gmail.com")

    print(pessoa1.apresenta())

if __name__ == "__name__":
    main()