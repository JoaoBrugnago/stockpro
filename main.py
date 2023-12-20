# Bibliotecas
import pandas as pd
import pymssql as sql
import warnings
import pyodbc
warnings.filterwarnings("ignore")

server = 'localhost'
database = 'Imediato'
username = 'sa'
password = 'joaosoares2007'
driver = '{SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE vendas (
    vndcode INT,
    rctcode INT,
    vndvalunitario FLOAT,
    vnddate DATE,
    PRIMARY KEY (vndcode, rctcode)
)
'''

cursor.execute(create_table_query)
conn.commit()
conn.close()
