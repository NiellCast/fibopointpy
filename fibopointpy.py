from data_request import FiboPoint
from info import Empresas
from os import system, name


empresa = Empresas()
while True:
	print()
	try:
		system('cls' if name == 'nt' else 'clear')
		ativo = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))
		
		system('cls' if name == 'nt' else 'clear')
		timeframe = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
		print()

		iniciar = FiboPoint(ativo=ativo, timeframe=timeframe)
		
		system('cls' if name == 'nt' else 'clear')
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		print(f'Ponto de Pivot em {ativo.upper()} de {empresa.nomes(ativo.upper())}.')
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		
		for item, preco in iniciar.calculo().items():
			print(f'{item.capitalize().replace("_", " ")}: {preco:.2f}')
			
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		print()
		
	except AttributeError:
		print('DIGITE OS DADOS CORRETAMENTE!')
		print()
		
	continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
	print()

	if continuar == 'N':
		break
