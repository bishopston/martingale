import requests
import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%Y%m%d')
days = ['26']
for day in days:

    url_prefix = 'https://www.athexgroup.gr/el/web/guest/statistics-end-of-day-indices/-/closing-prices/Ndr6R2dyheRO/txt/2021-11-'
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

    colnames = ['DATE', 'ISIN', 'SYMBOLGR', 'SYMBOL', 'CLOSE', 'OPEN', 'VOLUME', 'VALUE', 'HIGH', 'LOW', 'OPENINT', 'WEEKDIFF', 'MONTHDIFF', 'YEARDIFF']
    df = pd.read_csv(url,
                    encoding="ISO-8859-7", names=colnames, delim_whitespace=True,
                    header = 0, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], parse_dates=['DATE'], date_parser=dateparse)
					
    df.drop(['ISIN', 'SYMBOLGR', 'VALUE', 'OPENINT', 'WEEKDIFF', 'MONTHDIFF', 'YEARDIFF'], axis = 1, inplace=True)
    df['DATE'] = df['DATE'].dt.strftime('%Y/%m/%d')

    df = df.replace({'FTSE':'FTSE.ATH',
                    'GD':'GD.ATH',
                    'DTR':'DTR.ATH'})

    df = df[df['SYMBOL'].isin(['FTSE.ATH', 'GD.ATH', 'DTR.ATH'])]

    df['OPEN'] = 0.0000

    df = df[['SYMBOL', 'DATE', 'HIGH', 'LOW', 'OPEN', 'CLOSE', 'VOLUME']]
    
    df.to_csv('C:/helex_scraping/index_scraping/index_insert_files/df_index%s.txt' % day, index=None, sep='|', header=False)

    #type *.txt > index_concat.csv