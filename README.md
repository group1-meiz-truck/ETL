# ETL
ETL Project using meiz truck company data

## Description
 Meiz Trucks is a corporate trucks dealer with its head
office in the United States.
They sell trucks of different makes and models to
resellers and final users located in Nigeria.
The trucks are valued in the company’s local currency
(USD), but are sold in the customer’s local currency.



## Tools:
1. PostgreSql
2. Pandas
3. AWS Data Lake (S3 Bucket)
4. AWS DATA Warehouse (Redshift Service)
5. Python
6. Boto3

## steps
- Fetch data from PostgreSQL to AWS S3 using Pandas and Boto3
- Copy tables from S3 to Redshift (Raw Schema) using Python-Redshift Connector
- Run create statements in the Warehouse’s staging environment
- Transform dataset to fit the defined Star Schema
- Load the data into the staging environment with SQL