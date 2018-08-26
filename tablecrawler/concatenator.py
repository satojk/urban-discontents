import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina-Faso', 'Burundi', 'Cameroon', 'Cape-Verde-Cabo-Verde', 'Central-African-Republic', 'Chad', 'Comoros', 'Congo-Republic', 'Cote-dIvoire', 'Democratic-Republic-of-Congo', 'Djibouti', 'Egypt', 'Equatorial-Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea-Republic', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mayotte-France', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Reunion-France', 'Rwanda', 'Sao-Tome-e-Principe', 'Senegal', 'Seychelles', 'Sierra-Leone', 'Somalia', 'South-Africa', 'South-Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe', 'Afghanistan', 'Bangladesh', 'Bhutan', 'Brunei-Darussalam', 'Cambodia', 'China', 'Democratic-Peoples-Republic-North-Korea', 'Hong-Kong-China', 'India', 'Indonesia', 'Iran', 'Japan', 'Kazakhstan', 'Kyrgyzstan', 'Laos', 'Macau-China', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar-formerly-Burma', 'Nepal', 'Pakistan', 'Philippines', 'Republic-South-Korea', 'Singapore', 'Sri-Lanka', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkmenistan', 'Uzbekistan', 'Vietnam', 'Anguilla-United-Kingdom', 'Antigua-and-Barbuda', 'Aruba-Netherlands', 'Bahamas', 'Barbados', 'Cayman-Islands-United-Kingdom', 'Cuba', 'Curaçao-Netherlands', 'Dominica', 'Dominican-Republic', 'Grenada', 'Guadeloupe-France', 'Haiti', 'Jamaica', 'Martinique-France', 'Puerto-Rico-USA', 'Sint-Maarten-Netherlands', 'St-Kitts-and-Nevis', 'St-Lucia', 'St-Vincent-and-the-Grenadines', 'Trinidad-and-Tobago', 'Virgin-Islands-United-Kingdom', 'Virgin-Islands-USA', 'Belize', 'Costa-Rica', 'El-Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia-and-Herzegovina-Federation', 'Bosnia-and-Herzegovina-Republika-Srpska', 'Bulgaria', 'Croatia', 'Cyprus-Republic', 'Czech-Republic', 'Denmark', 'Estonia', 'Faeroe-Islands-Denmark', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar-United-Kingdom', 'Greece', 'Guernsey-United-Kingdom', 'Hungary', 'Iceland', 'Ireland-Republic', 'Isle-Man-United-Kingdom', 'Italy', 'Jersey-United-Kingdom', 'KosovoKosova', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia-former-Yugoslav-Republic', 'Malta', 'Moldova-Republic', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian-Federation', 'San-Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United-Kingdom-England-Wales', 'United-Kingdom-Northern-Ireland', 'United-Kingdom-Scotland', 'Bahrain', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Qatar', 'Saudi-Arabia', 'Syria', 'United-Arab-Emirates', 'Yemen', 'Bermuda-United-Kingdom', 'Canada', 'Greenland-Denmark', 'United-States-America', 'American-Samoa-USA', 'Australia', 'Cook-Islands-New-Zealand', 'Fiji', 'French-Polynesia-France', 'Guam-USA', 'Kiribati', 'Marshall-Islands', 'Micronesia-Federated-States', 'Nauru', 'New-Caledonia-France', 'New-Zealand', 'Northern-Mariana-Islands-USA', 'Palau', 'Papua-New-Guinea', 'Samoa', 'Solomon-Islands', 'Timor-Leste-formerly-East-Timor', 'Tonga', 'Tuvalu', 'Vanuatu', 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'French-GuianaGuyane-France', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

relevant_countries = ['italy', 'united-states-america', 'brazil', 'canada', 'france', 'israel',
'south-africa', 'macau-china']


def basic():
    master_df = pd.DataFrame()
    for country in countries:
        country = country.lower()
        print(country)
        try:
            df = pd.read_csv('output/{}_basic.csv'.format(country),
                             header=0, index_col=0)
            master_df = pd.concat([master_df, df], axis=1, sort=False)
        except FileNotFoundError:
            print('File not found. Skipping...')
    master_df = master_df[sorted(master_df.columns)]
    master_df.to_csv('output/processed/basic.csv')

def prisonpop():
    master_df = pd.DataFrame()
    for country in countries:
        country = country.lower()
        print(country)
        try:
            df = pd.read_csv('output/{}_prisonpop.csv'.format(country),
                             header=0, index_col=0)
            df = pd.concat({country: df}, axis=1, names=['country', 'info'], sort=False)
            master_df = pd.concat([master_df, df], axis=1, sort=False)
        except FileNotFoundError:
            print('File not found. Skipping...') #TODO change to use blank col
    master_df = master_df[sorted(master_df.columns)]
    master_df.to_csv('output/processed/prisonpop.csv')

def relevant_prisonpop():
    master_df = pd.DataFrame()
    for country in relevant_countries:
        country = country.lower()
        print(country)
        try:
            df = pd.read_csv('output/{}_prisonpop.csv'.format(country),
                             header=0, index_col=0)
            #df = pd.DataFrame({country: df['Prison population rate (per 100,000 of national population)']/100000.0})
            df = pd.DataFrame({country: df['Prison population total']})
            _df = pd.read_csv('output/{}_furtherPri.csv'.format(country),
                             header=0, index_col=0)
            #_df = pd.DataFrame({country: _df['Prison population rate (per 100,000 of national population)']/100000.0})
            _df = pd.DataFrame({country: _df['Prison population total']})
            _df = _df[~_df.index.duplicated(keep='first')]
            df = pd.concat([df, _df], axis=0, sort=False)
            df = df.set_index(pd.Index(map(lambda x: int(str(x).split('-')[0]), df.index)))
            df = df.sort_index()
            df = df[~df.index.duplicated(keep='first')]
            print(type(df))
            #print(master_df)
            master_df = pd.concat([master_df, df], axis=1, sort=False, join='outer')
        except FileNotFoundError:
            print('File not found. Skipping...') #TODO change to use blank col
    master_df = master_df.interpolate()
    master_df = master_df[sorted(master_df.columns)]
    master_df.to_csv('output/processed/relevant_prisonpop.csv')
    master_df.plot()
    plt.show()

relevant_prisonpop()
