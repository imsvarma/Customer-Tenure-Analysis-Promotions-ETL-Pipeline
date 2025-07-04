# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 12:40:14 2025

@author: imani
"""

import pandas as pd
import datetime
from sqlalchemy import *
from db_connection import engine

file_path="C:/Users/imani/Downloads/customers-100.csv"

#Extract

def extract(file_path):
    df=pd.read_csv(file_path)
    print('Extracted ',len(df),'rows')
    return df

def transform(df):
    #lets caliculate tenure date
    
    df['Subscription Date']=pd.to_datetime(df['Subscription Date'])
    today=pd.to_datetime('today')
    df['Tenure']=(today-df['Subscription Date']).dt.days/365.25
    df['Tenure']=df['Tenure'].round(2)
    print(df.head())
    
    #New df Full name
    df['Full Name']=df['First Name'] +' '+ df['Last Name']
    print(df.head())
    
    #Customer Segment
    df['Segment']=df['Tenure'].apply(segment_tenure)
    print(df.head())
    print(df.tail())
    
    #drop Index column
    df = df.drop(columns=['Index'])
    
    return df
    
    
def segment_tenure(years):
    if years <3.5:
        return 'New'
    else:
        return 'Loyal'
    

df=extract(file_path)
df=transform(df)

print(df.columns)

# all the columns as a customer table
#engine=db_connection.engine
#df.to_sql('Customer', con=engine, if_exists='replace', index=False)




metadata=MetaData()
customer_table = Table('Customer',metadata,
        Column('Customer Id',String(50),primary_key=True    ),
        Column('Full Name', String(150)),
        Column('Country',String(25)),
        Column('Tenure',DECIMAL(20)),
        Column('Segment',String(10))
        
                       )
df_selected=df[['Customer Id','Full Name','Tenure','Country','Segment']]

metadata.create_all(engine)

df_selected.to_sql('Customer',con=engine,if_exists='replace',index=False)



















