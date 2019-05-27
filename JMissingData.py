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
data = pd.read_pickle('data/pickles//states_data_pandas.pickle')
tx_data = data['TX NSA Value']
tx_data_annual = tx_data.resample('A').mean()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
df_tx = pd.DataFrame(tx_data)
df_tx.columns = ['monthly']
df_tx['annual'] = tx_data_annual
# df_tx.dropna(inplace=True)
# df_tx.fillna(value=-99999,inplace=True)
df_tx.fillna(method='ffill',inplace=True)
print(df_tx)
df_tx['monthly'].plot(ax=ax1, label='monthly report', linestyle='-', linewidth=1)
df_tx['annual'].plot(ax=ax1, label='annual mean report',linestyle='-', linewidth=2)
plt.legend()
plt.show()
