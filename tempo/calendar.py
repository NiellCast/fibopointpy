from datetime import date, timedelta


class Data:
	def __init__(self) -> None:
		self._data = date.today()
		
	def pegar_data_inicial(self, dias: int) -> str:
		"""
		:param dias: Recebe a quantidade de dias para subtrair e calcular data - dias.
		:return: Retorna a data do dia anterior em formato de string (dia/mês/ano).
		"""

		subtracao = timedelta(days=dias)

		inicial = self._data - subtracao
		inicial = inicial.strftime('%d/%m/%Y')
		
		return inicial
		
	def pegar_data_atual(self) -> str:
		"""
		:return: Retorna a data atual em tipo string (dia/mês/ano).
		"""
		return self._data.strftime('%d/%m/%Y')
