from tabula import read_pdf

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

yrs = ['13', '14', '15', '16', '17', '18']

for yr in yrs:
    for month in months:
        print(yr, month)
        df = read_pdf('beds/bed_capacity_{}{}.pdf'.format(month, yr))
        df.to_csv('output/bed_capacity_{}{}.csv'.format(month, yr), index=False)
