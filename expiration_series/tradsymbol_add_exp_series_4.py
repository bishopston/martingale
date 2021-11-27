import pandas as pd
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df1 = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_" + latest + "_expand.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['trading_symbol','asset','optiontype', 'strike', 'expmonthdate'])

df1.drop(['trading_symbol', 'strike'], axis = 1, inplace=True)

df2 = pd.read_csv("C:/helex_scraping/expseries/expseries_with_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['expseries_id','asset','optiontype', 'expmonthdate', 'created_at'])

df2.drop(['expseries_id'], axis = 1, inplace=True)

COLS = ['asset', 'optiontype', 'expmonthdate']

#print(df1[~df1[COLS].isin(df2[COLS].to_dict(orient='list')).all(axis=1)])

df_new_expseries = df1[~df1[COLS].isin(df2[COLS].to_dict(orient='list')).all(axis=1)]

assets = df_new_expseries.asset.unique()
optiontypes = df_new_expseries.optiontype.unique()
expdates = df_new_expseries.expmonthdate.unique()

df_new_expseries_ = pd.DataFrame(columns=['asset','optiontype','expmonthdate'])

for j in range(len(assets)):
    for x in range(len(optiontypes)):
        for y in range(len(expdates)):
            #df_series = df.loc[(df['asset'] == assets[j]) & (df['optiontype'] == optiontypes[x]) & (df['expmonthdate'] == expdates[y])]
            #print(str(dates[i]) + " " + str(df_series['vol'].sum()) + " " + str(assets[j]) + " " + str(optiontypes[x]) + " " + str(expdates[y]) + " " + str(df_series['trades'].sum()) + " " + str(df_series['open_interest'].sum()))
            
            df_new_expseries_.loc[-1] = [assets[j] , optiontypes[x] , expdates[y]]
            df_new_expseries_.index = df_new_expseries_.index + 1
            df_new_expseries_ = df_new_expseries_.sort_index()

created_at = {"created_at":[]}
for item in df_new_expseries_['asset']:
    created_at["created_at"].append(datetime.today().strftime("%Y-%m-%d"))

df_new_expseries_ = df_new_expseries_.assign(created_at = created_at["created_at"])

print(df_new_expseries_)
df_new_expseries_.to_csv("C:/helex_scraping/expseries/new_expseries_4.csv", index=None, sep='|', header=False)