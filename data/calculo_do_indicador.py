from investpy import get_stocks


class PontoDePivot:
    def __init__(self, ativo: str):
        self.__acoes = list(get_stocks('brazil')['symbol'])
        self.__ativo = ativo

    def calcular_indicador(self, maxima, minima, fechamento, abertura_do_dia) -> dict:
        """
        :return: Retorna um dicionário com os dados de Suporte, Resistência e Ponto de Pivot.
        """

        if self.__ativo in self.__acoes:
            pivot_point = round((maxima + minima + fechamento) / 3, 2)

            r1 = round(abertura_do_dia + ((maxima - minima) * .618), 2)
            r2 = round(abertura_do_dia + ((maxima - minima) * 1), 2)
            r3 = round(abertura_do_dia + ((maxima - minima) * 1.618), 2)

            s1 = round(abertura_do_dia - ((maxima - maxima) * .618), 2)
            s2 = round(abertura_do_dia - ((maxima - minima) * 1), 2)
            s3 = round(abertura_do_dia - ((maxima - minima) * 1.618), 2)

            return {
                'resistencia_3': r3,
                'resistencia_2': r2,
                'resistencia_1': r1,
                'pivot_point': pivot_point,
                'suporte_1': s1,
                'suporte_2': s2,
                'suporte_3': s3
            }
