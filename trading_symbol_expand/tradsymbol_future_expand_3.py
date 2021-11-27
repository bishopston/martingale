import pandas as pd
import numpy as np
import re
import calendar
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df = pd.read_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_future_check_for_new_symbol.csv", sep='|',
                encoding="ISO-8859-7",
                names=['trading_symbol'])

symbol = {"asset":[], "expdate":[]}

def expirationMonth(capital): 
    switcher = { 
        "A": 1, 
        "B": 2, 
        "C": 3, 
        "D": 4, 
        "E": 5, 
        "F": 6, 
        "G": 7, 
        "H": 8, 
        "I": 9, 
        "J": 10, 
        "K": 11, 
        "L": 12,
        "AX": 1, 
        "BX": 2, 
        "CX": 3, 
        "DX": 4, 
        "EX": 5, 
        "FX": 6, 
        "GX": 7, 
        "HX": 8, 
        "IX": 9, 
        "JX": 10, 
        "KX": 11, 
        "LX": 12,
        "LY": 12,
    } 
    return switcher.get(capital)

# Switcher for expirationYear to extract exp year and build exp date
def expirationYear(year): 
    switcher = { 
        "19": 2019, 
        "20": 2020, 
        "21": 2021, 
        "22": 2022, 
        "23": 2023,
        "24": 2024, 
        "25": 2025, 
        "26": 2026, 
        "27": 2027, 
        "28": 2028, 
        "29": 2029, 
        "30": 2030,
    } 
    return switcher.get(year)

c = calendar.Calendar(firstweekday=calendar.SUNDAY)

for item in df['trading_symbol']:
    _AZSplit = re.split('[A-Z]', item)
    _09Split = re.split('[0-9]', item)
    symbol["asset"].append(_09Split[0])
    #depending on last capital (e.g. "F" or "FX"), year might be selected either as [-2] or [-3]
    if _AZSplit[-2] != '':
        year = expirationYear(_AZSplit[-2])
    else:
        year = expirationYear(_AZSplit[-3])
    month = expirationMonth(_09Split[2])
    monthcal = c.monthdatescalendar(year,month)
    third_friday = [day for week in monthcal for day in week if
                day.weekday() == calendar.FRIDAY and
                day.month == month][2]
    symbol["expdate"].append(third_friday)

df = df.assign(asset = symbol["asset"], expdate = symbol["expdate"])
df = df[['trading_symbol', 'asset', 'expdate']]

created_at = {"created_at":[]}
for item in df['trading_symbol']:
    created_at["created_at"].append(datetime.today().strftime("%Y-%m-%d"))

df = df.assign(created_at = created_at["created_at"])

df.to_csv("C:/helex_scraping/tradsymbol_primkey/tradsymbol_future_" + latest + "_expand_3.csv", index=None, sep='|', header=False)