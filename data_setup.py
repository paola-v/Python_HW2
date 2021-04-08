import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from config import username, password

# CONNECT TO THE MYSQL DATABASE
engine = create_engine(f'mysql+pymysql://{username}:{password}@localhost/dogs_db')


# READING CSV FILE WITH DOGS INFO
dogs_df=pd.read_csv('dogs.csv')
print(dogs_df)


# READING CSV FILE WITH OWNERS INFO
owners_df=pd.read_csv('owners.csv')
print(owners_df)

# LOADING DATAFRAMES TO MYSQL TABLES
dogs_df.to_sql('dogs',engine,if_exists='append',index=False)
owners_df.to_sql('owners',engine,if_exists='append',index=False)