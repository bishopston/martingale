import requests
import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%d/%m/%Y')
days = ['26']
for day in days:

    url_prefix = 'https://www.athexgroup.gr/el/web/guest/statistics-end-of-day-securities/-/closing-prices/DV1cNobUfObV/txt/2021-11-'
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

    colnames = ['SYMBOL', 'DATE', 'CLOSE', 'AP', 'VOLUME', 'HIGH', 'LOW', 'VALUE', 'TRANS', 'OPEN', 'ISIN']
    df = pd.read_csv(url,
                    encoding="ISO-8859-7", names=colnames, delim_whitespace=True,
                    header = 0, usecols=[0,1,2,3,4,5,6,7,8,9,10], parse_dates=['DATE'], date_parser=dateparse)
					
    df.drop(['AP', 'VALUE', 'TRANS', 'ISIN'], axis = 1, inplace=True)

    df = df.replace({'ΑΔΜΗΕ':'ADMIE.ATH',
                    'ΑΛΦΑ':'ALPHA.ATH',
                    'ΜΠΕΛΑ':'BELA.ATH',
                    'CENER':'CENER.ATH',
                    'ΕΕΕ':'EEE.ATH',
                    'ΕΛΛΑΚΤΩΡ':'ELLAKTOR.ATH',
                    'ΕΛΠΕ':'ELPE.ATH',
                    'ΕΤΕ':'ETE.ATH',
                    'ΕΥΡΩΒ':'EUROB.ATH',
                    'ΕΧΑΕ':'EXAE.ATH',
                    'ΕΥΔΑΠ':'EYDAP.ATH',
                    'ΦΡΛΚ':'FOYRK.ATH',
                    'ΓΕΚΤΕΡΝΑ':'GEKTERNA.ATH',
                    'ΟΤΕ':'HTO.ATH',
                    'ΙΝΛΟΤ':'INLOT.ATH',
                    'ΙΝΤΚΑ':'INTRK.ATH',
                    'ΛΑΜΔΑ':'LAMDA.ATH',
                    'ΜΙΓ':'MIG.ATH',
                    'ΜΟΗ':'MOH.ATH',
                    'ΜΥΤΙΛ':'MYTIL.ATH',
                    'ΟΠΑΠ':'OPAP.ATH',
                    'ΟΛΠ':'PPA.ATH',
                    'ΔΕΗ':'PPC.ATH',
                    'ΑΤΤ':'TATT.ATH',
                    'ΤΕΝΕΡΓ':'TENERGY.ATH',
                    'ΠΕΙΡ':'TPEIR.ATH',
                    'ΒΙΟ':'VIO.ATH',
                    'TITC':'TITC.ATH'})

    df = df[df['SYMBOL'].isin(['ADMIE.ATH', 'ALPHA.ATH', 'BELA.ATH', 'CENER.ATH', 'EEE.ATH', 'ELLAKTOR.ATH', 'ELPE.ATH',
                            'ETE.ATH', 'EUROB.ATH', 'EXAE.ATH', 'EYDAP.ATH', 'FOYRK.ATH', 'GEKTERNA.ATH', 'HTO.ATH',
                            'INLOT.ATH', 'INTRK.ATH', 'LAMDA.ATH', 'MIG.ATH', 'MOH.ATH', 'MYTIL.ATH', 'OPAP.ATH',
                            'PPA.ATH', 'PPC.ATH', 'TATT.ATH', 'TENERGY.ATH', 'TPEIR.ATH', 'VIO.ATH', 'TITC.ATH'])]

    #df['DATE'] = pd.to_datetime(df.DATE)
    df['DATE'] = df['DATE'].dt.strftime('%Y-%m-%d')

    df = df[['SYMBOL', 'DATE', 'HIGH', 'LOW', 'OPEN', 'CLOSE', 'VOLUME']]
    
    df.to_csv('C:/helex_scraping/stock_scraping/stocks_insert_files/df_stocks%s.txt' % day, index=None, sep='|', header=False)

    #type *.txt > stock_concat.csv
