__author__ = "Daniell Castelo Branco Ciriaco"
__email__ = "niellcast.contato@outlook.com"

from data.data_request import FiboPoint
from names.search_name_by_code import NomeDasEmpresas
from install_requirements.instalacao import Instalacao
from style.style_functions import Estilo


def main() -> None:
	empresa = NomeDasEmpresas()

	while True:
		Estilo.pular_linha()

		try:
			Estilo.limpar_tela()

			ativo = str(input('Digite o código da ação que você quer calcular (ex: "MGLU3"): '))

			Estilo.limpar_tela()
			timeframe = str(input('Calcular no timeframe diário ou no semanal? [D/S]: '))
			Estilo.pular_linha()

			indicador = FiboPoint(ativo=ativo, timeframe=timeframe)
			tamanho = 28 + len(empresa.nome(ativo.upper()))

			Estilo.limpar_tela()
			print("=" * tamanho)
			print(f'Ponto de Pivot em {ativo.upper()} de {empresa.nome(ativo.upper())}.')
			print("=" * tamanho)

			for item, preco in indicador.receber_dados().items():
				print(f'{item.capitalize().replace("_", " ")}: {preco:.2f}')

			print("=" * tamanho)
			Estilo.pular_linha()

		except AttributeError:
			Estilo.limpar_tela()

			print("=" * tamanho)
			print(f'{"TIME FRAME INCORRETO!":^{tamanho}}')
			print(f'{"APENAS D ou S SÃO ACEITOS!":^{tamanho}}')
			print("=" * tamanho)

			Estilo.pular_linha()

		except TypeError:
			Estilo.limpar_tela()

			print("=" * 40)
			print(f'{"DADOS INCORRETOS FORAM DIGITADOS":^40}')
			print("=" * 40)

			Estilo.pular_linha()

		continuar = str(input('Continuar calculando? [S/N]: ')).strip().upper()
		Estilo.pular_linha()

		if continuar == 'N':
			break


if __name__ == '__main__':
	Estilo.limpar_tela()
	Instalacao.instalar_requisitos()
	main()
