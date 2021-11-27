import pandas as pd
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df1 = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_" + latest + "_expand.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['trading_symbol','asset','optiontype', 'strike', 'expmonthdate'])

df2 = pd.read_csv("C:/helex_scraping/expseries/expseries_with_id.csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['expseries_id','asset','optiontype', 'expmonthdate', 'created_at'])

df_merge = pd.merge(df1, df2, on=['asset','optiontype', 'expmonthdate'])

created_at = {"created_at":[]}
for item in df_merge['trading_symbol']:
    created_at["created_at"].append(datetime.today().strftime("%Y-%m-%d"))

df_merge = df_merge.assign(created_at = created_at["created_at"])

print(df_merge.head())

df_merge.to_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_" + latest + "_add_exp_series_with_id_2.csv", index=None, sep='|', header=False)