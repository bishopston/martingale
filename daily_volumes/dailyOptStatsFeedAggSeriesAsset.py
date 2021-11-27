import pandas as pd
import numpy as np
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df = pd.read_csv("C:/helex_scraping/dailyOptionStats/daily_opt_stats_agg_series_" + latest + ".csv", sep='|',
                encoding="ISO-8859-7",
                names=['date', 'asset', 'optiontype', 'vol', 'trades', 'open_interest'])
                
#for item in df['date']:
    #item = datetime.strptime(item, '%Y-%m-%d').date

df.drop(['asset'], axis = 1, inplace=True)

dates = df.date.unique()
#assets = df.asset.unique()
#expdates = df.expdate.unique()
optiontypes = df.optiontype.unique()

df_dailystats = pd.DataFrame(columns=['date','optiontype','vol','trades','open_interest'])

#series_list = [list(x) for x in zip(dates, assets, optiontypes)]

for i in range(len(dates)):
    #for j in range(len(assets)):
        for x in range(len(optiontypes)):
            #for y in range(len(expdates)):
                df_series = df.loc[(df['date'] == dates[i]) & (df['optiontype'] == optiontypes[x])]
                #print(str(dates[i]) + " " + str(df_series['vol'].sum()) + " " + str(assets[j]) + " " + str(optiontypes[x]) + " " + str(df_series['trades'].sum()) + " " + str(df_series['open_interest'].sum()))
                
                df_dailystats.loc[-1] = [dates[i], optiontypes[x] , df_series['vol'].sum() , df_series['trades'].sum() , df_series['open_interest'].sum()]
                df_dailystats.index = df_dailystats.index + 1
                df_dailystats = df_dailystats.sort_index()

print(df_dailystats.head())

df_dailystats.to_csv("C:/helex_scraping/dailyOptionStats/daily_opt_stats_agg_series_asset_" + latest + ".csv", index=None, sep='|', header=False)