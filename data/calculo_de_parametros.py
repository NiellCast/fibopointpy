from tempo.calendar import Data


class Calculo:
    def __init__(self, timeframe: str) -> None:
        self.__timeframe = timeframe.strip().upper()
        self.__tempo = Data()

    def calcular_parametros(self) -> list:
        """
        :return: Retorna uma lista contendo o timeframe escolhido de forma técnica
         e a data subtraída pela quantidade de dias.
        """

        if self.__timeframe == 'S':
            return ['Weekly', self.__tempo.pegar_data_inicial(14)]

        elif self.__timeframe == 'D':
            return ['Daily', self.__tempo.pegar_data_inicial(3)]
