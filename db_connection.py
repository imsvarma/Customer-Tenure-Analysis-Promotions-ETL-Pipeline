# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 23:57:28 2025

@author: imani
"""
from sqlalchemy import create_engine

server = 'MANIKANTAVARMA'
database= 'ETL_AVS_Practice'
driver = 'ODBC Driver 17 for SQL Server'
connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver.replace(' ', '+')}&trusted_connection=yes"
engine = create_engine(connection_string)
