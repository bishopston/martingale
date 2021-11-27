def ATMStrikeCalc(stock_price, strike_set):

    #stock_price = 1569.34
    #strike_set = [1050,	1075,	1100,	1125,	1150,	1175,	1200,	1225,	1250,	1275,	1300,	1325,	1350,	1375,	1400,	1425,	1450,	1475,	1500,	1525,	1550,	1575,	1600,	1625,	1650,	1675,	1700,	1725,	1750,	1775,	1800,	1825,	1850,	1875,	1900,	1925,	1950,	1975,	2000,	2050,	2100,	2150,	2200,	2250,	2300,	2350,	2400,	2450,	2500,	2550,	2600,
    #]

    #strikes_diff = [x - stock_price for x in strikes]

    return min(strike_set, key=lambda x:abs(x-stock_price))


