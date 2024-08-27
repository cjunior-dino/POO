class Mae:
    def __init__(self, nome_mae, sobrenome_mae):
        self.nome_mae = nome_mae
        self.sobrenome_mae = sobrenome_mae

    def exibir_informacoes_mae(self):
        return f"Mãe: {self.nome_mae} {self.sobrenome_mae}"