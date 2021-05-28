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
		elif timeframe.strip().upper() == 'D':
			self.timeframe = 'Daily'
		
		self.ativo = ativo.strip().upper()
		self.__acoes = list(get_stocks('brazil')['symbol'])
	
	def __dados(self) -> list:
		"""
		:return: Busca os dados históricos dos preços para cada ativo e retorna a máxima e a mínima do último candle.
		"""
		calendar = Data()
		try:
			grafico = get_stock_historical_data(stock=self.ativo,
			                                    country='brazil',
			                                    from_date=f'01/12/{calendar.ano() - 1}',
			                                    to_date=f'{calendar.dia()}/{calendar.mes()}/{calendar.ano()}',
			                                    interval=self.timeframe)
			
			# Insere o nome das colunas e limpa o desnecessário.
			grafico.columns = ['Abertura', 'Maxima', 'Minima', 'Fechamento', 'Volume', 'Moeda']
			grafico.drop(['Abertura', 'Fechamento', 'Moeda', 'Volume'], axis=1, inplace=True)
			
			return [grafico['Maxima'][-1], grafico['Minima'][-1]]
		
		except Exception:
			print('Não foi possível buscar os dados.')
	
	def calculo(self) -> dict:
		"""
		:return: Retorna um dicionário com os dados de Suporte, Resistência e Pivot.
		"""
		if self.ativo in self.__acoes:
			dados = self.__dados()
			pivot_point = round(sum(dados) / len(dados), 2)
			diferenca = dados[0] - dados[1]  # Máxima - Mínima
			s1 = round(pivot_point - 0.382 * diferenca, 2)
			s2 = round(pivot_point - 0.618 * diferenca, 2)
			s3 = round(pivot_point - 1 * diferenca, 2)
			r1 = round(pivot_point + 0.382 * diferenca, 2)
			r2 = round(pivot_point + 0.618 * diferenca, 2)
			r3 = round(pivot_point + 1 * diferenca, 2)
			
			return {'pivot_point': pivot_point,
			        'suporte_1': s1,
			        'suporte_2': s2,
			        'suporte_3': s3,
			        'resistencia_1': r1,
			        'resistencia_2': r2,
			        'resistencia_3': r3}
