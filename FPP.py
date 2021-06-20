from fibopoint import FiboPoint
from empresas import Empresas

empresa = Empresas()
while True:
	print()
	try:
		ativo = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))
		timeframe = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
		print()

		iniciar = FiboPoint(ativo=ativo, timeframe=timeframe)
		
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		print(f'Ponto de Pivot em {ativo.upper()} de {empresa.nomes(ativo.upper())}.')
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		
		for item, preco in iniciar.calculo().items():
			print(f'{item.capitalize().replace("_", " ")}: {preco:.2f}')
			
		print("=" * (28 + len(empresa.nomes(ativo.upper()))))
		print()
		
	except AttributeError:
		print('Digite os dados corretamente!')
		print()
		
	continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
	print()

	if continuar == 'N':
		break
