import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('fivethirtyeight')


def print_line(c, l):
    x = ''
    for i in range(0,l):
        x = x + c
    print(x)


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader('XOM', 'iex', start, end)

print_line('-',50)
print(df.head())

print_line('-',50)
print(df.tail(3))

df.reset_index(inplace=True)
df.set_index("date", inplace=True)
df = df.drop("volume", axis=1)

print_line('-',50)
print(df.head())

df[['high','low']].plot()
plt.legend()
plt.show()
