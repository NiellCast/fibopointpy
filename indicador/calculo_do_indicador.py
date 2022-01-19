from data.data_request import MarketData
from data.verificar_ativo import Verificacao


class PontoDePivot:
    @staticmethod
    def calcular_indicador(ativo: str) -> dict:
        """
        :return: Retorna um dicionário com os dados de Suporte, Resistência e Ponto de Pivot.
        """

        if Verificacao.verificar(ativo):
            dados = MarketData(ativo)

            maxima = dados.receber_dados()['maxima_anterior']
            minima = dados.receber_dados()['minima_anterior']
            fechamento = dados.receber_dados()['fechamento_anterior']
            abertura_do_dia = dados.receber_dados()['abertura_do_dia']

            pivot_point = round((maxima + minima + fechamento) / 3, 2)

            r1 = round(abertura_do_dia + ((maxima - minima) * .618), 2)
            r2 = round(abertura_do_dia + ((maxima - minima) * 1), 2)
            r3 = round(abertura_do_dia + ((maxima - minima) * 1.618), 2)
            r4 = round(abertura_do_dia + ((maxima - minima) * 2), 2)

            s1 = round(abertura_do_dia - ((maxima - minima) * .618), 2)
            s2 = round(abertura_do_dia - ((maxima - minima) * 1), 2)
            s3 = round(abertura_do_dia - ((maxima - minima) * 1.618), 2)
            s4 = round(abertura_do_dia - ((maxima - minima) * 2), 2)

            return {
                'resistencia_4': r4,
                'resistencia_3': r3,
                'resistencia_2': r2,
                'resistencia_1': r1,
                'pivot_point': pivot_point,
                'suporte_1': s1,
                'suporte_2': s2,
                'suporte_3': s3,
                'suporte_4': s4
            }
