import pandas as pd

DATA_URLPATH = "https://raw.githubusercontent.com/moi96-git/21DM004-Computing-for-Data-Science/refs/heads/main/data/covid.csv"

def load_rawdata(url):
    return pd.read_csv(url)


def filter_numactive(df_data, greaterthan):
    return df_data.loc[df_data['Active'] > greaterthan]


def calc_deathratio(df_data):
    df_new = df_data.copy()
    df_new['Deaths/Confirmed'] = df_new['Deaths'] / df_new['Confirmed']
    return df_new


if __name__ == "__main__":
    df_test = load_rawdata(DATA_URLPATH)
    active_values = [500, 1000, 5000]
    for x in active_values:
        df_filter = filter_numactive(df_test, x)
        df_calc = calc_deathratio(df_filter)
        avgratio = df_calc['Deaths/Confirmed'].mean()
        print(f"Countries with more than {x} active cases (n={df_filter['Country'].count()}): {df_filter['Country'].to_list()}")
        print(f"Average death/confirmed ratio among these countries: {avgratio}")


