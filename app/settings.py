from os import mkfifo, getenv

api_key = getenv('BINANCE_APIKEY', '')
api_secret = getenv('BINANCE_SECRET_KEY', '')
tld = "com"

telegram_token = getenv('TELEGRAM_TOKEN', '')
telegram_chatid = getenv('TELEGRAM_CHATID', '')

trade_coin = getenv('TRADE_COIN', 'BUSD')
trade_limit_coin_balance = getenv('TRADE_COIN_LIMIT_BALANCE')
trade_crypto = getenv('TRADE_CRYPTO', 'BTC')
trade_time_frame = getenv('TRADE_TIME_FRAME', "15m")
trade_market = getenv('TRADE_MARKET', 0)

trade_rsi_ifr = int(getenv('TRADE_RSI_IFR', 14))
trade_rsi_stochastic = int(getenv('TRADE_RSI_STOCH', 14))
trade_rsi_k = int(getenv('TRADE_RSI_K', 3))
trade_rsi_d = int(getenv('TRADE_RSI_D', 3))

trade_ema_cross = int(getenv('TRADE_EMA_CROSS', 0))
trade_ema_low = int(getenv('TRADE_EMA_LOW', 2))
trade_ema_high = int(getenv('TRADE_EMA_HIGH', 4))

trade_ema_base_candle = int(getenv('TRADE_EMA_BASE_CANDLE', 0))
trade_ema_base_candle_value = int(getenv('TRADE_EMA_BASE_CANDLE_VALUE', 8))
trade_ema_base_candle_qtd = int(getenv('TRADE_EMA_BASE_CANDLE_QTD', 2))

trade_wma_cross = int(getenv('TRADE_WMA_CROSS', 0))
trade_wma_low = int(getenv('TRADE_WMA_LOW', 2))
trade_wma_middle = int(getenv('TRADE_WMA_MIDDLE', 10))
trade_wma_high = int(getenv('TRADE_WMA_HIGH', 11))
trade_wma_cross_candle_qtd = int(getenv('TRADE_WMA_CROSS_CANDLE_QTD', 2))

notification_only = getenv('NOTIFICATION_ONLY', 1)
