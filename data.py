__author__ = "Daniell Castelo Branco Ciriaco"
__email__ = "niellcast.contato@outlook.com"

from datetime import date, timedelta


class Data:
	def __init__(self, dias: int) -> None:
		"""
		:param dias: Recebe a quantidade de dias para subtrair e calcular data - dias.
		"""
		
		self.data = date.today()
		self.subtracao = timedelta(days=dias)
		
	def data_inicial(self) -> str:
		"""
		:return: Retorna a data do dia anterior em formato de string (dia/mês/ano)
		"""
		
		inicial = self.data - self.subtracao
		inicial = inicial.strftime('%d/%m/%Y')
		
		return inicial
		
	def data_atual(self) -> str:
		hoje = self.data.strftime('%d/%m/%Y')
		
		return hoje
