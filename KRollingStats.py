import quandl as qd
import pandas as pd
import pickle
import matplotlib.pyplot as plt
api_key = open('data//key_store//quandl_key.txt','r').read()


def get_states():
    wiki_source = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
    columns = [''] * 13
    columns[1] = 'abbr'
    wiki_source.columns = columns
    states = wiki_source['abbr'].tolist()
    return states


def fetch_data_init():
    main_df = pd.DataFrame()
    states = get_states()
    for state in states:
        df = qd.get('FMAC/HPI_'+state, auth_token=api_key)
        df.columns = [[state + ' NSA Value', state + ' SA Value']]
        print('FMAC/HPI_'+state)
        if main_df.empty:
            main_df = df[state+' NSA Value']
        else:
            main_df = main_df.join(df[state+' NSA Value'])

    main_df.to_pickle('data//pickles//states_data_pandas.pickle')


#fetch_data_init()
#STD VS DATA TEXAS
'''
data = pd.read_pickle('data/pickles//states_data_pandas.pickle')
tx_data = data['TX NSA Value']
tx_data_annual = tx_data.rolling(12).mean()
tx_data_std = tx_data.rolling(12).std()
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0))
df_tx = pd.DataFrame(tx_data)
df_tx.columns = ['monthly']
df_tx['RMA12'] = tx_data_annual
df_tx['STD12'] = tx_data_std

print(df_tx)
df_tx['monthly'].plot(ax=ax1, label='monthly report')
df_tx['RMA12'].plot(ax=ax1, label='RMA12 report')
df_tx['STD12'].plot(ax=ax2, label="STD12 report")
plt.legend()
plt.show()'''

data = pd.read_pickle('data/pickles//states_data_pandas.pickle')
tx_data = data['TX NSA Value']
ak_data = data['AK NSA Value']
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
tx_data.columns =['texas data']
ak_data.columns =['alaska data']
aktx_df = pd.DataFrame(tx_data)
aktx_df['alaska data'] = ak_data
tx_al_12_corr = tx_data.rolling(12).corr(ak_data)

print(aktx_df)
aktx_df['texas data'].plot(ax=ax1, label="texas data")
aktx_df['alaska data'].plot(ax=ax1, label="alaska data")
ax1.legend(loc=4)
tx_al_12_corr.plot(ax=ax2, label="correlation")
plt.legend(loc=4)
plt.show()
