import quandl
import quandlconfig

OHLC_TABLE = "WIKI/PRICES"

# authenticate with quandl
quandl.ApiConfig.api_key = quandlconfig.API_KEY


data = quandl.get_table(OHLC_TABLE, date='2017-12-27', qopts = { "columns" : [ "ticker","date","open","high","low","close","volume"]}, paginate = True )
print ("pause")