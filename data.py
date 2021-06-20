from datetime import date, timedelta


class Data:
	def __init__(self, dias: int) -> None:
		self.data = date.today()
		self.subtracao = timedelta(days=dias)
		
	def ontem(self) -> str:
		ontem = self.data - self.subtracao
		ontem = ontem.strftime('%d/%m/%Y')
		
		return ontem
		
	def hoje(self) -> str:
		hoje = self.data.strftime('%d/%m/%Y')
		
		return hoje

