import pandas as pd
import psycopg2
import redshift_connector
from sqlalchemy import create_engine
from configparser import ConfigParser
import boto3

from utils.helper import create_bucket, connect_to_dwh
from sql_statements.create import raw_data_tables
from sql_statements.transform import transformation_queries
from sql_statements.create import transformed_tables


config = ConfigParser()
config.read('.env')

region = config['AWS']['region']
bucket_name = config['AWS']['bucket_name']
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']

host = config['DB_CRED']['host']
user = config['DB_CRED']['username']
password = config['DB_CRED']['password']
database = config['DB_CRED']['database']

dwh_host = config['DWH']['host']
dwh_user = config['DWH']['username']
dwh_password = config['DWH']['password']
dwh_database = config['DWH']['database']
dwh_role = config['DWH']['role']
# create our bucket
# create_bucket()
# extract from database to our datalake
#conn = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{database}') 

s3_path = 's3://{}/{}.csv'
tables = ['customers', 'banks', 'items', 'transactions', 'exchange_rates']


#for table in tables:

#    query = f'SELECT * FROM {table}'
#    df = pd.read_sql_query(query, conn)

#    df.to_csv(
#        s3_path.format(bucket_name, table)
#        , index=False
#        , storage_options={
#            'key': access_key
#            , 'secret': secret_key
#        }
#    )

# step 3: Create the raw schema in dwh
# connection to redshift
conn_details = {
  'host': dwh_host
   , 'user': dwh_user
   , 'password': dwh_password
   , 'database': dwh_database
}

dwh_conn = connect_to_dwh(conn_details)
print('conn successful')


cursor = dwh_conn.cursor()



dev_schema = 'raw_data'
staging_schema = 'staging'

cursor.execute(f'CREATE SCHEMA {dev_schema}')
dwh_conn.commit()

for query in raw_data_tables:
   # print(f'------------------------{query[:50]}')
    cursor.execute(query)
    dwh_conn.commit()


for table in tables:
    query = f'''
    copy {dev_schema}.{table} 
    from '{s3_path.format(bucket_name, table)}'
    iam_role '{dwh_role}'
    delimiter ','
    ignoreheader 1;
    '''
    cursor.execute(query)
    dwh_conn.commit()

# for table in tables:
#     cursor.execute(f''''
#         COPY {dev_schema}.{table}
#         FROM 's3://{bucket_name}/{table}.csv'
#         IAM_ROLE '{dwh_role}'
#         REGION '{region}'
#         DELIMITER ','
#         IGNOREHEADER 1;
#         ''')


# dwh_conn.commit()



# step 4
cursor.execute(f'''CREATE SCHEMA {staging_schema}''')
dwh_conn.commit()

for query in transformed_tables:
    cursor.execute(query)
    dwh_conn.commit()


for query in transformation_queries:
    print(f'------------------------{query[:50]}')
    cursor.execute(query)
    dwh_conn.commit()


# step 5: Data Quality Check
staging_tables = ['dim_customers', 'dim_items', 'dim_banks,dim_dates', 'ft_customer_transactions' ]
query = 'SELECT COUNT(*) FROM staging.{}'

for table in staging_tables:
    cursor.execute(query.format(table))
    print(f'Table {table} has {cursor.fetchall()}')



cursor.close()
dwh_conn.close()


