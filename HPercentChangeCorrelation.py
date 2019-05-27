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
        base = df['NSA Value'][0]
        df.columns = [[state + ' NSA Value', state + ' SA Value']]
        print('FMAC/HPI_'+state)
        df[state+' NSA Value'] = ((df[state+' NSA Value']-base)/base)*100
        if main_df.empty:
            main_df = df[state+' NSA Value']
        else:
            main_df = main_df.join(df[state+' NSA Value'])

    main_df.to_pickle('data//pickles//states_data_pandas.pickle')


def fetch_data_usa():
    df = qd.get("FMAC/HPI_USA", authtoken=api_key)
    df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] * 100.0
    return df['NSA Value']


fetch_data_init()
mean_state = fetch_data_usa()
data = pd.read_pickle('data//pickles//states_data_pandas.pickle')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
data.plot(ax=ax1)
mean_state.plot(color='k', ax=ax1, linewidth=5)
plt.legend().remove()
plt.show()
data_correlation = data.corr()
print(data_correlation)
print(data_correlation.describe())

data_correlation.to_csv('data//csv_store//data_corr.csv')

data_correlation.describe().to_csv('data//csv_store//data_corr_desc.csv')
