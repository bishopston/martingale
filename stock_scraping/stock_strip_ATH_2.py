import pandas as pd

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df = pd.read_csv("C:/helex_scraping/scalper_backup/scalper2_stocks_" + latest + ".csv", sep='|',
                   encoding="ISO-8859-7",
                   names=['symbol','date','high','low','open','close','volume'])


dict_asset = {"asset":[]}

for item in df['symbol']:
    stripped_symbol = item.replace('.ATH','')
    dict_asset["asset"].append(stripped_symbol)

df = df.assign(asset = dict_asset["asset"])

df = df[['symbol','asset','date','high','low','open','close','volume']]

df.to_csv('c:/helex_scraping/scalper_backup/scalper2_stocks_' + latest + '_stripped_ATH.csv', header=None, index=None, sep='|')