from os import system, name


def limpar() -> None:
	system('cls' if name == 'nt' else 'clear')


def pular(x: int = 1) -> None:
	for linha in range(x):
		print()

