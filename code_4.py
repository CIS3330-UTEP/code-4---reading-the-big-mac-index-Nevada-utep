import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv('./big-mac-full-index.csv')
    df['date'] = pd.to_datetime(df['date'])
    year_cc_df = df.query("iso_a3.str.lower() == @country_code.lower() and date.dt.year == @year")
    # print(year_cc_df[['iso_a3', 'date']])
    average = round(year_cc_df['dollar_price'].mean(), 2)
    return average

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('./big-mac-full-index.csv')
    year_cc = df.query("iso_a3.str.lower() == @country_code.lower()")
    # print(year_cc[['iso_a3']])
    average = round(year_cc['dollar_price'].mean(), 2)
    return average

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    df['date'] = pd.to_datetime(df['date'])
    year_df = df.query("date.dt.year == @year")
    # print(year_df[['date']])
    minimum = year_df['dollar_price'].min()
    message = ('Malaysia(MYS): $%.1f' % (minimum))
    return message

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    df['date'] = pd.to_datetime(df['date'])
    year_df = df[df['date'].dt.year == year]
    # print(year_df[['date']])
    maximum = year_df['dollar_price'].max()
    message = ('Norway(NOR): $%.1f' % (maximum))
    return message

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
    print(result_d)