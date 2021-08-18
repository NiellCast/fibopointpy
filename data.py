from datetime import date, timedelta


class Data:
	def __init__(self, dias: int) -> None:
		"""
		:param dias: Recebe a quantidade de dias para subtrair e calcular data - dias.
		"""
		
		self.data = date.today()
		self.subtracao = timedelta(days=dias)
		
	def ontem(self) -> str:
		"""
		:return: Retorna a data do dia anterior em formato de string (dia/mês/ano)
		"""
		
		ontem = self.data - self.subtracao
		ontem = ontem.strftime('%d/%m/%Y')
		
		return ontem
		
	def hoje(self) -> str:
		hoje = self.data.strftime('%d/%m/%Y')
		
		return hoje
