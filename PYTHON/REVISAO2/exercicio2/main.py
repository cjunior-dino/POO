from classe_gato import Gato
from classe_cachorro import Cachorro


def main():
    gato = Gato()

    cachorro = Cachorro()

    print(gato.fazer_som())
    print(cachorro.fazer_som())

if __name__ == "__main__":
    main()