import pandas as pd
import numpy as np


def print_line(char, length):
    line = ''
    for i in range(0,length):
        line = line + char
    print(line)


df = pd.read_csv('data//stocks.csv')
print(df.head())
df.reset_index()
df.set_index('date', inplace=True)

print_line('-',50)
print(df.tail(10))
df.tail(10).to_csv('data//new_stocks.csv')

df2 = pd.read_csv('data//new_stocks.csv', index_col=0)
print_line('-',50)
print(df2.tail())

df2.columns = [['Company Name','Stock Value']]
print_line('-', 50)
print(df2.head())
df2.to_csv('data//noheader_stocks.csv', header=False)
df2.to_html('data//htmlio.html')

df3 = pd.read_csv('data//stocks.csv', names=['Company', 'Value'], index_col=1, skiprows=[0])
print_line('-',50)
print(df3.head())
df3.columns = [['cname','value']]
print_line('-',50)
print(df3.tail())

df3.rename(columns ={'cname':'Company Name','value':'Company Value'},inplace=True)
print_line('-',50)
print(df3.head())
