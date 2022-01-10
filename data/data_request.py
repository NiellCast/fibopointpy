from investpy import get_stock_historical_data
from tempo.calendar import Data
from data.calculo_de_parametros import Calculo
from calculo_do_indicador import PontoDePivot


class FiboPoint:
	def __init__(self, ativo: str, timeframe: str) -> None:
		"""
		:param ativo: Digitar o código da ação que deseja calcular.
		:param timeframe: Digitar qual timeframe (D - Diário, S - Semanal) quer calcular.
		"""
		self.__calc = Calculo(timeframe)
		self.__tempo = Data()

		self.__ativo = ativo.strip().upper()
		self.__indicador = PontoDePivot(ativo)

	def receber_dados(self) -> dict:
		"""
		:return: Busca os dados históricos dos preços para cada ativo e retorna a máxima e a mínima do último candle.
		"""

		grafico = get_stock_historical_data(stock=self.__ativo, country='brazil',
											from_date=self.__calc.calcular_parametros()[1],
											to_date=self.__tempo.pegar_data_atual(),
											interval=self.__calc.calcular_parametros()[0])

		# Insere o nome das colunas e limpa o desnecessário.
		grafico.columns = ['Abertura', 'Maxima', 'Minima', 'Fechamento', 'Volume', 'Moeda']
		grafico.drop(['Moeda', 'Volume'], axis=1, inplace=True)

		maxima = grafico['Maxima'][-2]
		minima = grafico['Minima'][-2]
		fechamento = grafico['Fechamento'][-2]
		abertura = grafico['Abertura'][-1]

		return self.__indicador.calcular_indicador(maxima, minima, fechamento, abertura)


a = FiboPoint('BBDC3', 'D')
print(a.receber_dados())
