class Triangulos:
    def __init__(self) -> None:
        pass

    def qual_triangulo(self, a,b,c):
        if a == b == c != 0:
            return "É um Triangulo equilátero"
        elif ((a == b  != c) or (a == c != b) or (b == c != a)) and ( a and b and c) != 0:
            return " É um Triangulo isósceles"
        elif (a != b != c) and (a and b and c) != 0:
            return 'É um triangulo escaleno' 
        else:
            return "Não é um triangulo"
            

