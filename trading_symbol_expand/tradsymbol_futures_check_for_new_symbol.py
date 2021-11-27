import pandas as pd

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()
#get the total dataframe including greeks as input and reduce it to include on trading_symbol
df1 = pd.read_csv("C:/helex_scraping/scalper_backup/futures_" + latest + "_stockmerge_symbolsplit_exact_expdate.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['new_trading_symbol', 'date', 'asset', 'expdate', 'closing_price','change','volume','max','min','trades','fixing_price','open_interest', 'spot_price'])
df1.drop(['date', 'asset', 'expdate', 'closing_price','change','volume','max','min','trades','fixing_price','open_interest', 'spot_price'], axis = 1, inplace=True)
#get the latest output from option_pricing_optionsymbol table
df2 = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/futuresymbol_with_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['trading_symbol_id','trading_symbol','asset', 'expmonthdate', 'created_at'])

df1 = df1.assign(flag=df1.new_trading_symbol.isin(df2.trading_symbol).values.astype(int))
df2 = df1.loc[df1['flag'] == 0]

del df2['flag']

df2.drop_duplicates(subset ="new_trading_symbol", 
                     keep = 'first', inplace = True)

df2.to_csv('C:/helex_scraping/tradsymbol_primkey/tradsymbol_future_check_for_new_symbol.csv', index=None, sep='|', header=False)
