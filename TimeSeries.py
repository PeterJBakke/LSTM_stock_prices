from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import pandas as pd

class Prices:
    def __init__(self, stock_symbol='.DJI', interval='86400', stock_exchange_symbol='INDEXDJX', period='1Y'):
        self.param = {
            'q': stock_symbol,
            'i': interval,
            'x': stock_exchange_symbol,
            'p': period
        }

    def get_prices(self):
        return get_price_data(self.param)


if __name__ == '__main__':
    myData = Prices(stock_symbol='OMXC20CAP', stock_exchange_symbol='INDEXNASDAQ')
    dowJones = pd.DataFrame(myData.get_prices())
    print(dowJones)