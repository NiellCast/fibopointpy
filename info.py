from investpy import get_stocks


class Empresas:
	def __init__(self) -> None:
		self._nomes = get_stocks('brazil')['name']
		self._simbolos = get_stocks('brazil')['symbol']

	def nome(self, codigo: str) -> list:
		"""
		:param codigo: Recebe o código da ação de uma empresa.
		:return: Retorna o nome da empresa baseado no código inserido.
		"""

		name_by_code = dict([(self._simbolos[contador], ativo) for contador, ativo in enumerate(self._nomes)])
		
		return name_by_code.get(codigo)
