from src.market_data.request_data import MarketData
from typing import Dict


class PivotPoint:
    @staticmethod
    def calculate(stock: str) -> Dict:
        """
        :return: Returns a dictionary with Support, Resistance and Pivot Point price.
        """

        market_data = MarketData(stock)

        high = market_data.get_data()['high']
        low = market_data.get_data()['low']
        close = market_data.get_data()['close']
        open_ = market_data.get_data()['open']

        pivot_point_price = round((high + low + close) / 3, 2)

        r1 = round(open_ + ((high - low) * .618), 2)
        r2 = round(open_ + ((high - low) * 1), 2)
        r3 = round(open_ + ((high - low) * 1.618), 2)
        r4 = round(open_ + ((high - low) * 2), 2)

        s1 = round(open_ - ((high - low) * .618), 2)
        s2 = round(open_ - ((high - low) * 1), 2)
        s3 = round(open_ - ((high - low) * 1.618), 2)
        s4 = round(open_ - ((high - low) * 2), 2)

        return {
            'resistencia_4': r4,
            'resistencia_3': r3,
            'resistencia_2': r2,
            'resistencia_1': r1,
            'pivot_point': pivot_point_price,
            'suporte_1': s1,
            'suporte_2': s2,
            'suporte_3': s3,
            'suporte_4': s4
        }

