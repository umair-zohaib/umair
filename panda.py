from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.types import String

engine = create_engine('postgresql://postgres:CFUmair123@localhost:5432/lyft_daily')
apr_csv_data = pd.read_csv('lyft_daily.csv')
apr_csv_data.rename( columns={'Unnamed: 0':'id'}, inplace=True )
#print(apr_csv_data.head())
apr_csv_data.to_sql('daily', engine, if_exists='append', index=False)