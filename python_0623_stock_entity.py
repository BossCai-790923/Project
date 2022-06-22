class stock:

    def __init__(self, index, ticker, name):
        self.name = name
        self.ticker = ticker
        self.index = index

    def get_ticker_value(self):
        return self.ticker.split(".")[0]

    def get_market(self):
        str = self.ticker.split(".")[1]
        if str == 'sh':
            return "SHANGHAI"
        else:
            return "SHENZHEN"

    def __str__(self):
        return f'stock(id={self.index}, ticker={self.ticker}, name={self.name})'

    def __repr__(self):
        return f'stock(id={self.index}, ticker={self.ticker}, name={self.name})'
