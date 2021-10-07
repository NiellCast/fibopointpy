import contextlib
from subprocess import call


class Instalacao:
	@staticmethod
	def instalar_requisitos() -> None:
		"""
		:return: Instala os requisitos automaticamente.
		"""

		with contextlib.suppress(Exception):
			call('pip install --upgrade -r requirements.txt')


if __name__ == '__main__':
	instalador = Instalacao()
	instalador.instalar_requisitos()
