from fibopoint import FiboPoint


while True:
	print()
	try:
		ativo = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))
		timeframe = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
		print()
	
		iniciar = FiboPoint(ativo=ativo, timeframe=timeframe)
	
		for item, preco in iniciar.calculo().items():
			print(f'{item.capitalize().replace("_", " ")}: {preco:.2f}')
		print()
		
	except Exception:
		print('Digite os dados corretamente!')
		print()
		
	continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
	print()
	
	if continuar == 'N':
		break
