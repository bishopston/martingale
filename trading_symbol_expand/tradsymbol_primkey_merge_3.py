import pandas as pd

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df1 = pd.read_csv("C:/helex_scraping/scalper_backup/scalper2_options_" + "900000" + "_incl_stock_iv_front_iv_greeks.csv", sep='|',
                encoding="ISO-8859-7",
                names=['trading_symbol', 'date', 'asset', 'optiontype', 'strike', 'expdate', 
                'closing_price', 'change', 'vol', 'max', 'min', 'trades', 'fixing_price', 
                'open_interest', 'close', 'implied_vol', 'strike_ATM', 'front_exp_date', 
                'imp_vol_exp', 'delta', 'theta', 'gamma', 'vega'])

df2 = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/optionsymbol_with_id_with_expseries_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['trading_symbol_id', 'trading_symbol', 'asset', 'optiontype', 'strike', 'expdate', 'expseriesid'])
df2.drop(['asset', 'optiontype', 'strike', 'expdate', 'expseriesid'], axis = 1, inplace=True)

df_merge = pd.merge(df1, df2, on=['trading_symbol'])
df_merge.drop(['trading_symbol','asset','optiontype','strike','expdate'], axis = 1, inplace=True)
df_merge = df_merge[['trading_symbol_id', 'date',
        'closing_price', 'change', 'vol', 'max', 'min', 'trades', 'fixing_price', 
        'open_interest', 'close', 'implied_vol', 'strike_ATM', 'front_exp_date', 
        'imp_vol_exp', 'delta', 'theta', 'gamma', 'vega']]

#print(df_merge.head())
df_merge.to_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_primkey_merge_" + "900000" + ".csv", index=None, sep='|', header=False)
