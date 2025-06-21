from binance import Client
from config import API_KEY, API_SECRET, TESTNET_URL
from loggers import get_logger

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        # self.client.FUTURES_URL = TESTNET_URL
        self.logger = get_logger()

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            return balance
        except Exception as e:
            self.logger.error(f"Balance Error: {str(e)}")
            return None
