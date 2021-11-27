import pandas as pd
import numpy as np
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df = pd.read_csv("C:/helex_scraping/scalper_backup/futures_" + latest + "_stockmerge_symbolsplit_exact_expdate.csv", sep='|',
                encoding="ISO-8859-7",
                names=['trading_symbol', 'date', 'asset', 'expdate', 'closing_price','change','volume','max','min','trades','fixing_price','open_interest','spot'])

df.drop(['trading_symbol','expdate','closing_price','change','max','min','trades','fixing_price','spot'], axis = 1, inplace=True)         

dates = df.date.unique()
assets = df.asset.unique()

df_histstats = pd.DataFrame(columns=['date','asset','volume','open_interest'])

for i in range(len(dates)):
    for j in range(len(assets)):
                df_series = df.loc[(df['date'] == dates[i]) & (df['asset'] == assets[j])]

                df_histstats.loc[-1] = [dates[i] , assets[j] , df_series['volume'].sum() , df_series['open_interest'].sum()]
                df_histstats.index = df_histstats.index + 1
                df_histstats = df_histstats.sort_index()

reversed_df_histstats = df_histstats.iloc[::-1]

print(reversed_df_histstats.head())

reversed_df_histstats.to_csv("C:/helex_scraping/dailyOptionStats/hist_future_stats_agg_asset_" + latest + ".csv", index=None, sep='|', header=False)