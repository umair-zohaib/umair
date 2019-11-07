from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:CFUmair123@localhost:5432/lyft_daily')
df = pd.read_csv('lyft_daily.csv')
df.rename(columns={'Unnamed: 0':'id'}, inplace=True )
df.to_sql('daily', engine, if_exists='replace', index=False)
df['year_month'] = pd.to_datetime(df['date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))
to_CSV = df.groupby(by=['company', 'brand', 'year_month']).agg({'transactions': 'sum', 'sales': 'sum'})
to_CSV.to_csv('trans_or_sales_sum.csv')


def split_column(b):
    brand_value = b.split()
    return brand_value[-1]


df['brand_remaining'] = df['brand'].apply(lambda x: split_column(x))


def merge_company_brand(m):
    merged_columns = ",".join(m[['company', 'brand']])
    return merged_columns


df['company_&_brand'] = df.apply(lambda x: merge_company_brand(x), axis=1)
print(df.head())
