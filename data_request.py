from investpy import get_stocks, get_stock_historical_data
from data import Data


class FiboPoint:
	def __init__(self, ativo: str, timeframe: str) -> None:
		"""
		:param ativo: Digitar o código da ação que deseja calcular.
		:param timeframe: Digitar qual timeframe (D - Diário, S - Semanal) quer calcular.
		"""
		
		if timeframe.strip().upper() == 'S':
			self.timeframe = 'Weekly'
			self.calendario = Data(14)
		elif timeframe.strip().upper() == 'D':
			self.timeframe = 'Daily'
			self.calendario = Data(3)
		
		self.ativo = ativo.strip().upper()
		self.__acoes = list(get_stocks('brazil')['symbol'])

	def dados(self) -> dict:
		"""
		:return: Busca os dados históricos dos preços para cada ativo e retorna a máxima e a mínima do último candle.
		"""
		
		grafico = get_stock_historical_data(stock=self.ativo,
		                                    country='brazil',
		                                    from_date=self.calendario.data_inicial(),
		                                    to_date=self.calendario.data_atual(),
		                                    interval=self.timeframe)
		
		# Insere o nome das colunas e limpa o desnecessário.
		grafico.columns = ['Abertura', 'Maxima', 'Minima', 'Fechamento', 'Volume', 'Moeda']
		grafico.drop(['Moeda', 'Volume'], axis=1, inplace=True)
		
		return {'maxima': grafico['Maxima'][-2], 'minima': grafico['Minima'][-2],
		        'fechamento': grafico['Fechamento'][-2], 'abertura': grafico['Abertura'][-1]}

	def calculo(self) -> dict:
		"""
		:return: Retorna um dicionário com os dados de Suporte, Resistência e Pivot.
		"""
		
		if self.ativo in self.__acoes:
			maxima = self.dados()['maxima']
			minima = self.dados()['minima']
			fechamento = self.dados()['abertura']
			
			pivot_point = round((maxima + minima + fechamento) / 3, 2)

			r1 = round(pivot_point + ((maxima - minima) * .382), 2)
			r2 = round(pivot_point + ((maxima - minima) * .618), 2)
			r3 = round(pivot_point + ((maxima - minima) * 1), 2)

			s1 = round(pivot_point - ((maxima - minima) - .382), 2)
			s2 = round(pivot_point - ((maxima - minima) - .618), 2)
			s3 = round(pivot_point - ((maxima - minima) - 1), 2)
			
			return {'pivot_point': pivot_point,
			        'suporte_1': s1,
			        'suporte_2': s2,
			        'suporte_3': s3,
			        'resistencia_1': r1,
			        'resistencia_2': r2,
			        'resistencia_3': r3}
