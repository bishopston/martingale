import pandas as pd

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df1 = pd.read_csv("C:/helex_scraping/scalper_backup/futures_" + latest + "_stockmerge_symbolsplit_exact_expdate.csv", sep='|',
                encoding="ISO-8859-7",
                names=['trading_symbol', 'date', 'asset', 'expdate', 'closing_price','change','volume','max','min','trades','fixing_price','open_interest', 'spot_price'])

df2 = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/futuresymbol_with_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['trading_symbol_id', 'trading_symbol', 'asset', 'expdate', 'created_at'])
df2.drop(['asset', 'expdate'], axis = 1, inplace=True)

df_merge = pd.merge(df1, df2, on=['trading_symbol'])
df_merge.drop(['trading_symbol','asset','expdate'], axis = 1, inplace=True)
df_merge = df_merge[['trading_symbol_id', 'date',
        'closing_price','change','volume','max','min','trades','fixing_price','open_interest', 'spot_price']]

df_merge.to_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_futures_primkey_merge_" + latest + ".csv", index=None, sep='|', header=False)
