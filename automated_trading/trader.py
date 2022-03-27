import matplotlib.pyplot as plt
import quandl as qd
from decouple import config

# pulls api key from .env file.
API_KEY = config('API_KEY')

# sets the api key for quandl.
qd.ApiConfig.api_key = API_KEY

# grabs BATS U.S. Stock Exchange for EDGX_RKLB
EDGX_RKLB_data = qd.get('BATS/EDGX_RKLB')

# assign 'Short Volume' to 'short_vol'
short_vol = EDGX_RKLB_data[['Short Volume']]

# returns as fractional change
daily_return = short_vol.pct_change()

# replacing NA values with 0
daily_return.fillna(0, inplace=True)

# caluclate the moving average
mav = short_vol.rolling(window=50).mean()

print('Daily Return\n\n{}\n'.format(daily_return))
print('Moving Average\n\n{}'.format(mav[-10:]))

short_vol.plot()
mav.plot()

plt.show()