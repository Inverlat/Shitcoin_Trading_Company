
from binance.client import Client



client = Client()
#klines = client.get_klines(symbol="BTCUSDT",interval=client.KLINE_INTERVAL_1MONTH)

klines = client.get_historical_klines(symbol="BTCUSDT",interval=client.KLINE_INTERVAL_1DAY, start_str=0)

Open_Time = [x[0] for x in klines] #0
Open = [x[1] for x in klines] #1
High = [x[2] for x in klines] #2
Low = [x[3] for x in klines] #3
Close = [x[4] for x in klines] #4
Volume = [x[5] for x in klines] #5
Close_Time = [x[6] for x in klines] #6
Quote_Asset_Volume = [x[7] for x in klines] #7
Number_Of_Trades = [x[8] for x in klines] #8
Taker_Buy_Base_Asset_Volume = [x[9] for x in klines] #9
Taker_Buy_Quote_Asset_Volume = [x[10] for x in klines] #10

Data_Frame = {
    "Open_Time": Open_Time,
    "Open": Open,
    "High": High,
    "Low": Low,
    "Close": Close,
    "Volume": Volume,
    "Close_Time": Close_Time,
    "Quote_Asset_Volume": Quote_Asset_Volume,
    "Number_Of_Trades": Number_Of_Trades,
    "Taker_Buy_Base_Asset_Volume": Taker_Buy_Base_Asset_Volume,
    "Taker_Buy_Quote_Asset_Volume": Taker_Buy_Quote_Asset_Volume
}