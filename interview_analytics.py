import pandas as pd
import pickle
import matplotlib.pyplot as plt


def read_csv():
    data_frame = pd.read_csv('data//100_sales_records.csv')
    data_frame.to_pickle('data//pickles//100_sale_records.pickle')


#read_csv()
df = pd.read_pickle('data//pickles//100_sale_records.pickle')
#row = input("enter row to fetch ")
#print(df.loc[int(row)])
#df.reset_index(inplace=True)
df['Date'] = pd.to_datetime(df['Ship Date'])
df = df.sort_values(by='Date')
df.reset_index()
df.set_index('Ship Date', inplace=True)
df = df.drop(columns=['Date'])
print(df.tail(5))
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
df['Units Sold'].plot(ax=ax1, label="sale data")
ax1.legend(loc=4)
plt.show()