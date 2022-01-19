from investpy import get_stock_historical_data
from tempo.calendar import Data


class MarketData:
    def __init__(self, ativo: str) -> None:
        self.__tempo = Data()
        self.__ativo = ativo

    def receber_dados(self) -> dict:
        """
        :return: Busca os dados históricos dos preços para cada ativo e retorna a máxima e a mínima do último candle.
        """

        grafico = get_stock_historical_data(
            stock=self.__ativo,
            country='brazil',
            from_date=self.__tempo.pegar_data_inicial(2),
            to_date=self.__tempo.pegar_data_atual(),
            interval='Daily'
        )

        # Insere o nome das colunas e exclui o desnecessário.
        grafico.columns = ['Abertura', 'Maxima', 'Minima', 'Fechamento', 'Volume', 'Moeda']
        grafico.drop(['Moeda', 'Volume'], axis=1, inplace=True)

        return {
            'maxima_anterior': grafico['Maxima'][-2],
            'minima_anterior': grafico['Minima'][-2],
            'fechamento_anterior': grafico['Fechamento'][-2],
            'abertura_do_dia': grafico['Abertura'][-1]
        }
