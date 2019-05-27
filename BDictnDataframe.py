import pandas as pd
import matplotlib.pyplot as plt


def print_line(c, l):
    x = ''
    for i in range(0,l):
        x = x + c
    print(x)


web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)
print_line('-',50)
print(df)

df.reset_index()
df.set_index('Day', inplace=True)
print_line('-',50)
print(df.drop('Bounce Rate', axis=1))
print_line('-',50)
print(df['Visitors'])
print_line('-',50)
print(df)
df.plot()
plt.show()
