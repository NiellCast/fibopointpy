__author__ = "Daniell Castelo Branco Ciriaco"
__email__ = "niellcast.contato@outlook.com"

from data_request import FiboPoint
from info import Empresas
from install import instalar_requisitos
from style.style_functions import pular, limpar


def run() -> None:
	empresa = Empresas()
	while True:
		pular()
		try:
			limpar()
			ativo = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))
			
			limpar()
			timeframe = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
			pular()
			
			iniciar = FiboPoint(ativo=ativo, timeframe=timeframe)
			tamanho = 28 + len(empresa.nomes(ativo.upper()))
			
			limpar()
			print("=" * tamanho)
			print(f'Ponto de Pivot em {ativo.upper()} de {empresa.nomes(ativo.upper())}.')
			print("=" * tamanho)
			
			for item, preco in iniciar.calculo().items():
				print(f'{item.capitalize().replace("_", " ")}: {preco:.2f}')
				
			print("=" * tamanho)
			pular()
			
		except AttributeError:
			limpar()
			
			print("=" * tamanho)
			print(f'{"TIME FRAME INCORRETO!":^{tamanho}}')
			print(f'{"APENAS D ou S SÃO ACEITOS!":^{tamanho}}')
			print("=" * tamanho)
			
			pular()
		
		except TypeError:
			limpar()
			
			print("=" * 40)
			print(f'{"DADOS INCORRETOS FORAM DIGITADOS":^40}')
			print("=" * 40)
			
			pular()
			
		continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
		pular()
	
		if continuar == 'N':
			break


if __name__ == '__main__':
	limpar()
	instalar_requisitos()
	run()
