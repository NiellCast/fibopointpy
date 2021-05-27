from datetime import date


class Data:
	def __init__(self) -> None:
		self.__hoje = date.today()
		
	def dia(self) -> int or str:
		return f'0{self.__hoje.day}' if self.__hoje.day < 10 else self.__hoje.day
	
	def mes(self) -> int or str:
		return f'0{self.__hoje.month}' if self.__hoje.month < 10 else self.__hoje.month
	
	def ano(self) -> int:
		return self.__hoje.year
