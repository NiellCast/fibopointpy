from os import system, name


class Estilo:
    @staticmethod
    def limpar_tela() -> None:
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def pular_linha(x: int = 1) -> None:
        for linha in range(x):
            print()
