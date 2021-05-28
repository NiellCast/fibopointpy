from FiboPoint import FiboPoint


while True:
	print()
	atv = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))
	tf = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
	print()
	iniciar = FiboPoint(ativo=atv, timeframe=tf)
	for item, dado in iniciar.calculo().items():
		print(f'{item.capitalize()}: {dado:.2f}')
	print()
	
	continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
	print()
	if continuar == 'N':
		break
