import quandl as qd
import pandas as pd

api_key = open('data//key_store//quandl_key.txt','r').read()

#df = qd.get("FMAC/HPI_AK", authtoken=api_key)
#print(df.head())

wiki_source = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
columns = [''] * 13
columns[1] = 'abbr'
wiki_source.columns = columns
states = wiki_source['abbr'].tolist()
api_url = []
for state in states:
    api_url.append('HPI_'+state)
print(api_url)
