from os import mkfifo, getenv

api_key = getenv('BINANCE_APIKEY', '')
api_secret = getenv('BINANCE_SECRET_KEY', '')
tld = "com"

telegram_token = getenv('TELEGRAM_TOKEN', '')
telegram_chatid = getenv('TELEGRAM_CHATID', '')

trade_coin = getenv('TRADE_COIN', 'BUSD')
trade_crypto = getenv('TRADE_CRYPTO', 'CHZ')

trade_rsi_ifr=int(getenv('TRADE_RSI_IFR', 14))
trade_rsi_stochastic=int(getenv('TRADE_RSI_STOCH', 14))
trade_rsi_k=int(getenv('TRADE_RSI_K', 3))
trade_rsi_d=int(getenv('TRADE_RSI_D', 3))
