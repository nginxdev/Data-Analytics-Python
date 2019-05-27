import quandl as qd
import pandas as pd
import pickle


def get_states():
    wiki_source = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
    columns = [''] * 13
    columns[1] = 'abbr'
    wiki_source.columns = columns
    states = wiki_source['abbr'].tolist()
    return states


def fetch_data_init():
    main_df = pd.DataFrame()
    api_key = open('data//key_store//quandl_key.txt','r').read()
    states = get_states()
    for state in states:
        df = qd.get('FMAC/HPI_'+state, auth_token=api_key)
        print('FMAC/HPI_'+state)
        df.columns = [[state+' NSA Value', state+' SA Value']]
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    # pickle_out = open('data//pickles//states_data.pickle', 'wb')
    # pickle.dump(main_df, pickle_out)
    # pickle_out.close()
    main_df.to_pickle('data//pickles//states_data_pandas.pickle')


# fetch_data_init()
# pickle_in = open('data//pickles//states_data.pickle', 'rb')
# data = pickle.load(pickle_in)
data = pd.read_pickle('data/pickles//states_data_pandas.pickle')
print(data)
