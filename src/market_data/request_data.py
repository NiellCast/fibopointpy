from investpy import get_stock_historical_data
from src.time.time_calculation import Date
from typing import Dict


class MarketData:
    def __init__(self, stock: str) -> None:
        self.__time = Date()
        self.__stock = stock

    def get_data(self) -> Dict:
        """
        :return: Search historical price data for each stock and return the high and low of the last candle.
        """

        stock_data = get_stock_historical_data(
            stock=self.__stock,
            country='brazil',
            from_date=self.__time.get_start_date(4),
            to_date=self.__time.get_current_date(),
            interval='Daily'
        )

        stock_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Currency']
        stock_data.drop(['Currency', 'Volume'], axis=1, inplace=True)

        return {
            'high': stock_data['High'][-2],
            'low': stock_data['Low'][-2],
            'close': stock_data['Close'][-2],
            'open': stock_data['Open'][-1]
        }
