from investpy import get_stocks


class Empresas:
	def __init__(self):
		self.empresas = get_stocks('brazil')
		
	def nomes(self, codigo):
		nomes_das_empresas = self.empresas["symbol"]
		
		lista = dict([(nomes_das_empresas[contador], ativo) for contador, ativo in enumerate(self.empresas['name'])])
		
		return lista.get(codigo)

