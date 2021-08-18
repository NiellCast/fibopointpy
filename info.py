from investpy import get_stocks


class Empresas:
	def __init__(self) -> None:
		self.empresas = get_stocks('brazil')
		
	def nomes(self, codigo: str) -> list:
		"""
		:param codigo: Recebe o código da ação de uma empresa.
		:return: Retorna o nome da empresa baseado no código inserido.
		"""
		nomes_das_empresas = self.empresas["symbol"]
		
		lista = dict([(nomes_das_empresas[contador], ativo) for contador, ativo in enumerate(self.empresas['name'])])
		
		return lista.get(codigo)
