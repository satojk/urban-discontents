import requests
from bs4 import BeautifulSoup
import csv
import os

base_url = 'http://app.vancouver.ca/EngWaterQuality_Net/OneStationReading.aspx?RegionID='

for region_id in range(1, 24):
    if region_id == 3: continue
    print('Working with id {}...'.format(region_id))
    url = base_url + str(region_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    region_name = soup.find(id='ctl00_cphMainContent_lblRegion').text
    region_name = ''.join(region_name.lower().split())
    print('Region: {}'.format(region_name))
    rows = soup.find_all('tr')
    header = [None, None]
    open_table = open('blank_table.csv', 'w+')
    for ix, row in enumerate(rows):
        if ix == 0:
            continue
        elif ix == 1:
            header[0] = [' '.join(th.text.split('\r\n')) for th in row.select('th')]
            print(header[0])
        elif ix == 2:
            header[1] = [th.text for th in row.select('th')]
            print(header[1])
        elif row.find(id='readingsStation'):
            station_name = row.find_all('th')[0].text.lower()
            station_name = station_name.replace('(', ' ').replace(')', ' ').strip()
            station_name = station_name.replace('/', '')
            station_name = ''.join(station_name.split())
            open_table.close()
            open_table = open('output/{}-{}.csv'.format(region_name, station_name), 'w+')
            wr = csv.writer(open_table)
            wr.writerows(header)
        else:
            wr = csv.writer(open_table)
            wr.writerows([[td.text for td in row.select('td')]])
    open_table.close()

os.remove('blank_table.csv')
