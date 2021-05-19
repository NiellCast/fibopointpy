import investpy
from datetime import date


class FiboPoint:
	def __init__(self, ativo):
		"""
		:param ativo: Digitar o código da ação que deseja calcular
		"""
		self.hoje = date.today()
		self.ativo = ativo.strip().upper()
		self.acoes = list(investpy.get_stocks('brazil')['symbol'])
	
	def data(self):
		hoje = self.hoje
		
		# Caso dia ou mês for menor que 10, retorna o dia com um 0 (zero) na frente.
		dia = f'0{hoje.day}' if hoje.day < 10 else hoje.day
		mes = f'0{hoje.month}' if hoje.month < 10 else hoje.month
		ano = hoje.year
		
		return [dia, mes, ano]
	
	def dados(self):
		try:
			grafico = investpy.get_stock_historical_data(stock=self.ativo,
			                                             country='brazil',
			                                             from_date=f'01/06/{self.data()[2] - 1}',
			                                             to_date=f'{self.data()[0]}/{self.data()[1]}/{self.data()[2]}',
			                                             interval='Daily')
			
			# Insere o nome das colunas e limpa o desnecessário.
			grafico.columns = ['Abertura', 'Maxima', 'Minima', 'Fechamento', 'Volume', 'Moeda']
			grafico.drop(['Abertura', 'Moeda', 'Volume'], axis=1, inplace=True)
			
			return [grafico['Maxima'][-1], grafico['Minima'][-1], grafico['Fechamento'][-1]]
			
		except Exception:
			print('Não foi possível buscar os dados.')
	
	def calculo(self):
		"""
		:return: Retorna um dicionário com os dados de Suporte, Resistência e Pivot.
		"""
		if self.ativo in self.acoes:
			dados = self.dados()
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


if __name__ == '__main__':
	iniciar = FiboPoint(ativo='MGLU3')
	print(iniciar.calculo())

