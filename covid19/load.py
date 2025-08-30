import pandas as pd
df = pd.read_csv('covid_data.csv')
df = df.dropna()
df.rename(columns={'Country/Region': 'Country'}, inplace=True)
print(df.info())
print("Total Cases:", df['Confirmed'].sum())
print("Total Deaths:", df['Deaths'].sum())
country_summary = df.groupby('Country')['Confirmed'].sum().sort_values(ascending=False)
print(country_summary)


