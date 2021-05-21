from datetime import date


class Data:
	def __init__(self):
		self.hoje = date.today()
		
	def dia(self):
		return f'0{self.hoje.day}' if self.hoje.day < 10 else self.hoje.day
	
	def mes(self):
		return f'0{self.hoje.month}' if self.hoje.month < 10 else self.hoje.month
	
	def ano(self):
		return self.hoje.year
