import pandas as pd
import numpy as np
from datetime import datetime

file1 = open("C:\helex_scraping\stock_scraping\latest_date.txt","r+")
latest = file1.read()

df = pd.read_csv("C:/helex_scraping/dailyOptionStats/daily_opt_stats_agg_series_asset_" + latest + ".csv", sep='|',
                encoding="ISO-8859-7",
                names=['date', 'optiontype', 'vol', 'trades', 'open_interest'])

months = [
    '2019-06-01',
    '2019-07-01',
    '2019-08-01',
    '2019-09-01',
    '2019-10-01',
    '2019-11-01',
    '2019-12-01',
    '2020-01-01',
    '2020-02-01',
    '2020-03-01',
    '2020-04-01',
    '2020-05-01',
    '2020-06-01',
    '2020-07-01',
    '2020-08-01',
    '2020-09-01',
    '2020-10-01',
    '2020-11-01',
    '2020-12-01',
    '2021-01-01',
    '2021-02-01',
    '2021-03-01',
    '2021-04-01',
    '2021-05-01',
    '2021-06-01',
    '2021-07-01',
    '2021-08-01',
    '2021-09-01',
    '2021-10-01',
    '2021-11-01',
    '2021-12-01',
    '2022-01-01',
    '2022-02-01',
    '2022-03-01',
    '2022-04-01',
    '2022-05-01',
    '2022-06-01',
    '2022-07-01',
    '2022-08-01',
    '2022-09-01',
    '2022-10-01',
    '2022-11-01',
    '2022-12-01',
    '2023-01-01',
    '2023-02-01',
    '2023-03-01',
    '2023-04-01',
    '2023-05-01',
    '2023-06-01',
    '2023-07-01',
    '2023-08-01',
    '2023-09-01',
    '2023-10-01',
    '2023-11-01',
    '2023-12-01',
    '2024-01-01',
    '2024-02-01',
    '2024-03-01',
    '2024-04-01',
    '2024-05-01',
    '2024-06-01',
    '2024-07-01',
    '2024-08-01',
    '2024-09-01',
    '2024-10-01',
    '2024-11-01',
    '2024-12-01',
    '2025-01-01',
    '2025-02-01',
    '2025-03-01',
    '2025-04-01',
    '2025-05-01',
    '2025-06-01',
    '2025-07-01',
    '2025-08-01',
    '2025-09-01',
    '2025-10-01',
    '2025-11-01',
    '2025-12-01',
]
df_months=[]
months_len = len(months)-1
for i in range(months_len):
    df_months.append(df[(df['date'] >= months[i]) & (df['date'] < months[i+1])])

df_callputmonthlysums=pd.DataFrame(columns=['date','optiontype','sum_vol'])

for i in range(len(df_months)):
    optiontypes = df_months[i].optiontype.unique()
    for j in range(len(optiontypes)):
        df_optiontype = df_months[i].loc[(df_months[i]['optiontype'] == optiontypes[j])]

        df_callputmonthlysums.loc[-1] = [months[i], optiontypes[j], df_optiontype['vol'].sum()]
        df_callputmonthlysums.index = df_callputmonthlysums.index + 1
        df_callputmonthlysums = df_callputmonthlysums.sort_index()

df_monthlycall = df_callputmonthlysums.loc[(df_callputmonthlysums['optiontype'] == 'c')]
df_monthlyput = df_callputmonthlysums.loc[(df_callputmonthlysums['optiontype'] == 'p')]
df_merge = pd.merge(df_monthlycall, df_monthlyput, on=['date'])
df_callputratio = df_merge[['sum_vol_x']].div(df_merge['sum_vol_y'], axis=0)
df_callputratio.rename(columns={'sum_vol_x':'CallPutRatio'},
                 inplace=True)
df_callputmonthlysumsratio = df_merge.join(df_callputratio)
df_callputmonthlysumsratio.drop(["optiontype_x", "optiontype_y"], axis = 1, inplace=True)
df_callputmonthlysumsratio.rename(columns={'sum_vol_x':'sum_vol_calls',
                'sum_vol_y':'sum_vol_puts'},
                 inplace=True)

reversed_df_callputmonthlysumsratio = df_callputmonthlysumsratio.iloc[::-1]

#print(reversed_df_callputmonthlysumsratio)
#print(reversed_df_callputmonthlysumsratio.iloc[[0]])
print(reversed_df_callputmonthlysumsratio[-1:])
reversed_df_callputmonthlysumsratio[-1:].to_csv("C:/helex_scraping/dailyOptionStats/callputmonthlysumsratio_" + latest + ".csv", index=None, sep='|', header=False)
#reversed_df_callputmonthlysumsratio.to_csv("C:/helex_scraping/dailyOptionStats/callputmonthlysumsratio_" + latest + ".csv", index=None, sep='|', header=False)