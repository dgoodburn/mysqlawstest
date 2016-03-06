__author__ = 'dangoodburn'


import pandas as pd
import instance
from sqlalchemy import create_engine

database = instance.getDatabase()
engine = create_engine(database)

df = pd.read_csv('elevationtest.csv')
df.to_sql('elevationtest', engine, if_exists = 'replace', index=False)