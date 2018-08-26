import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor

countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina-Faso', 'Burundi', 'Cameroon', 'Cape-Verde-Cabo-Verde', 'Central-African-Republic', 'Chad', 'Comoros', 'Congo-Republic', 'Cote-dIvoire', 'Democratic-Republic-of-Congo', 'Djibouti', 'Egypt', 'Equatorial-Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea-Republic', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte-France', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Reunion-France', 'Rwanda', 'Sao-Tome-e-Principe', 'Senegal', 'Seychelles', 'Sierra-Leone', 'Somalia', 'South-Africa', 'South-Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe', 'Afghanistan', 'Bangladesh', 'Bhutan', 'Brunei-Darussalam', 'Cambodia', 'China', 'Democratic-Peoples-Republic-North-Korea', 'Hong-Kong-China', 'India', 'Indonesia', 'Iran', 'Japan', 'Kazakhstan', 'Kyrgyzstan', 'Laos', 'Macau-China', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar-formerly-Burma', 'Nepal', 'Pakistan', 'Philippines', 'Republic-South-Korea', 'Singapore', 'Sri-Lanka', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkmenistan', 'Uzbekistan', 'Vietnam', 'Anguilla-United-Kingdom', 'Antigua-and-Barbuda', 'Aruba-Netherlands', 'Bahamas', 'Barbados', 'Cayman-Islands-United-Kingdom', 'Cuba', 'Curaçao-Netherlands', 'Dominica', 'Dominican-Republic', 'Grenada', 'Guadeloupe-France', 'Haiti', 'Jamaica', 'Martinique-France', 'Puerto-Rico-USA', 'Sint-Maarten-Netherlands', 'St-Kitts-and-Nevis', 'St-Lucia', 'St-Vincent-and-the-Grenadines', 'Trinidad-and-Tobago', 'Virgin-Islands-United-Kingdom', 'Virgin-Islands-USA', 'Belize', 'Costa-Rica', 'El-Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia-and-Herzegovina-Federation', 'Bosnia-and-Herzegovina-Republika-Srpska', 'Bulgaria', 'Croatia', 'Cyprus-Republic', 'Czech-Republic', 'Denmark', 'Estonia', 'Faeroe-Islands-Denmark', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar-United-Kingdom', 'Greece', 'Guernsey-United-Kingdom', 'Hungary', 'Iceland', 'Ireland-Republic', 'Isle-Man-United-Kingdom', 'Italy', 'Jersey-United-Kingdom', 'KosovoKosova', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia-former-Yugoslav-Republic', 'Malta', 'Moldova-Republic', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian-Federation', 'San-Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United-Kingdom-England-Wales', 'United-Kingdom-Northern-Ireland', 'United-Kingdom-Scotland', 'Bahrain', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Qatar', 'Saudi-Arabia', 'Syria', 'United-Arab-Emirates', 'Yemen', 'Bermuda-United-Kingdom', 'Canada', 'Greenland-Denmark', 'United-States-America', 'American-Samoa-USA', 'Australia', 'Cook-Islands-New-Zealand', 'Fiji', 'French-Polynesia-France', 'Guam-USA', 'Kiribati', 'Marshall-Islands', 'Micronesia-Federated-States', 'Nauru', 'New-Caledonia-France', 'New-Zealand', 'Northern-Mariana-Islands-USA', 'Palau', 'Papua-New-Guinea', 'Samoa', 'Solomon-Islands', 'Timor-Leste-formerly-East-Timor', 'Tonga', 'Tuvalu', 'Vanuatu', 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'French-GuianaGuyane-France', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

base_url = 'http://www.prisonstudies.org/country/'

def process_country(unformatted_country, base_url):
    def thunk():
        try:
            country = unformatted_country.lower()
            print('Working with country {}'.format(country))
            r = requests.get(base_url + country)
            soup = BeautifulSoup(r.content, 'html.parser')
            basic_data = soup.find(id='basic_data')
            first_tables = basic_data.find_all('table')
            rows = []
            rows.append([first_tables[0].select('tr th')[0].text,
                         first_tables[0].select('tr td')[0].text])
            rows += list(zip([h.text.strip() for h in first_tables[1].select('tr th')],
                             [d.text.strip() for d in first_tables[1].select('tr td')]))
            rows += list(zip([h.text.strip() for h in first_tables[2].select('tr th')],
                             [d.text.strip() for d in first_tables[2].select('tr td')]))
            with open('output/{}_basic.csv'.format(country), 'w+') as out_fp:
                wr = csv.writer(out_fp)
                wr.writerows(rows)

            rows = []
            rows.append(('Year', 'Prison population total', 'Prison population rate (per 100,000 of national population)'))
            rows += [tuple([td.text.strip().strip('c').strip().replace(',','') for
                     td in row.select('td')]) for
                     row in soup.find(id='views-aggregator-datatable').select('tr')[1:]]

            with open('output/{}_prisonpop.csv'.format(country), 'w+') as out_fp:
              wr = csv.writer(out_fp)
              wr.writerows(rows)

            tables = soup.find(id='further_info').find_all('table')

            tableids = [title.text[:3] for title in 
              soup.find(id='further_info').find_all('h3')]
            for ix, table in enumerate(tables):
                tableid = tableids[ix]
                rows = []
                for row in table.select('tr'):
                    entries = [entry.text.strip().replace(',', '') for entry in row.select('td')]
                    sub_lines_count = entries[0].count('\n')
                    for entry in entries:
                        if entry.count('\n') != sub_lines_count:
                            rows += [list(map(lambda x: ' '.join(x.split('\n')),
                            entries))]
                            break
                    else:
                        rows += list(map(tuple, zip(*(map(lambda x: x.split('\n'), 
                                                          entries)))))
                with open('output/{}_further{}.csv'.format(country, tableid), 'w+') as out_fp:
                    wr = csv.writer(out_fp)
                    wr.writerows(rows)
        except (AttributeError, IndexError) as e:
            print(e)
            print('Skipping...')

    return thunk

pool = ThreadPoolExecutor(max_workers=16)
for unformatted_country in countries:
    thunk = process_country(unformatted_country, base_url)
    _ = pool.submit(thunk)
pool.shutdown()
