import pandas as pd

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df1 = pd.read_csv("C:/helex_scraping/scalper_backup/" + latest + "_QUERY_STOCKS_EXPORT.csv", sep='|',
                encoding="ISO-8859-7",
                names=['symbol', 'date', 'high', 'low', 'open', 'close', 'volume'])

df2 = pd.read_csv("C:/helex_scraping/scalper_backup/stocksymbol_with_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['symbol_id', 'symbol', 'asset'])
df2.drop(['asset'], axis = 1, inplace=True)

#print(df1.dtypes)
#print(df2.dtypes)

df_merge = pd.merge(df1, df2, on=['symbol'])
df_merge.drop(['symbol'], axis = 1, inplace=True)
df_merge = df_merge[['symbol_id', 'date', 'high', 'low', 'open', 'close', 'volume']]

#print(df_merge.head())
df_merge.to_csv("C:/helex_scraping/scalper_backup/stock_primkey_merge_" + latest + ".csv", index=None, sep='|', header=False)
