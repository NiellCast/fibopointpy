__author__ = "Daniell Castelo Branco Ciriaco"
__email__ = "niellcast.contato@outlook.com"

from subprocess import call


def instalar_requisitos() -> None:
	try:
		call('pip install --upgrade -r requirements.txt')
	except Exception:
		print('Não foi possível instalar um ou mais requisitos. Tente instalá-los manualmente!')
		print()
		input('Aperte qualquer tecla para continuar!')


if __name__ == '__main__':
	instalar_requisitos()
