import requests
import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y%m%d')
days = ['26']
for day in days:

    url_prefix = 'https://www.athexgroup.gr/el/web/guest/statistics-end-of-day-derivatives/-/closing-prices/YkHkPR3hQJEG/txt/2021-11-'
    url = url_prefix + str(day)

    try:
        page_response = requests.get(url, timeout=5)

        if page_response.status_code == 200:
            print('Successful Connection')

        else:
            print(page_response.status_code)
        

    except requests.Timeout as e:
        print('Timeout occurred for requested page: ' + url)
        print(str(e))

    colnames = ['DATE', 'SYMBOL', 'CLOSE', 'DIFF', 'VOLUME', 'HIGH', 'LOW', 'TRANS', 'FIXING', 'OPENINT', 'BASESYMBOL']
    df = pd.read_csv(url,
                    encoding="ISO-8859-7", names=colnames, delim_whitespace=True,
                    header = 0, usecols=[0,1,2,3,4,5,6,7,8,9,10], parse_dates=['DATE'], date_parser=dateparse)
					
    df.drop(['BASESYMBOL'], axis = 1, inplace=True)

    df = df[['SYMBOL', 'DATE', 'CLOSE', 'DIFF', 'VOLUME', 'HIGH', 'LOW', 'TRANS', 'FIXING', 'OPENINT']]

    df['DATE'] = df['DATE'].dt.strftime('%Y/%m/%d')

    df['SYMBOL']= df['SYMBOL'].astype(str)

    df1 = df[(df['SYMBOL'].str.contains(".", regex=False))]
    df2 = df[(df['SYMBOL'].str.contains("FTSE", regex=False))]
    frames = [df1, df2]
    df_options = pd.concat(frames)
    df_options = df_options[df_options['SYMBOL'].apply(lambda x: len(x) > 8)]

    df_options.to_csv('C:/helex_scraping/option_scraping/options_insert_files/df_options%s.txt'  % day, index=None, sep='|', header=False)

    #type *.txt > option_concat.csv

    df3 = df[~(df['SYMBOL'].str.contains(".", regex=False))]
    df_futures = df3[df3['SYMBOL'].apply(lambda x: len(x) < 10)]

    df_futures.to_csv('C:/helex_scraping/option_scraping/futures_insert_files/df_futures%s.txt' % day, index=None, sep='|', header=False)

    #type *.txt > future_concat.csv
