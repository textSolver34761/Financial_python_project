import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like  # Allows for pandas_datareader to be imported
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime.now()
df = web.DataReader('GOOGL', 'morningstar', start, end)
#df.to_csv('google.csv')
df = pd.read_csv('google.csv', parse_dates=True, index_col=0)
print(df.head())

df['Open'].plot()
plt.show()
