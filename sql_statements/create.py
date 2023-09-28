
# =============================================== FOR DEV SCHEMA
customers = ''' CREATE TABLE IF NOT EXISTS raw_data.customers
(
    id integer PRIMARY KEY NOT NULL ,
    name character varying,
    email character varying,
    registered_at timestamp without time zone
); 
'''

banks = '''CREATE TABLE IF NOT EXISTS raw_data.banks
(
    _id character varying(50) PRIMARY KEY NOT NULL,
    code integer,
    name character varying(50)
        
);'''
	
items = ''' CREATE TABLE IF NOT EXISTS raw_data.items
(
	id integer PRIMARY KEY NOT NULL,
	name character varying(50),
	selling_price numeric(7,2),
	cost_price numeric(7,2)
); '''
	
transactions = '''	CREATE TABLE IF NOT EXISTS raw_data.transactions
(
	id integer PRIMARY KEY NOT NULL,
	customer_id integer ,
	item_id bigint ,
	date date ,
	bank_id character varying,
	qty integer
); '''
	
exchange_rates = '''	CREATE TABLE IF NOT EXISTS raw_data.exchange_rates
(
	id integer PRIMARY KEY NOT NULL,
	customer_id integer ,
	item_id bigint ,
	date date ,
	bank_id character varying,
	qty integer
); '''	
	
# =============================================== FOR STAR SCHEMA

dim_customers = '''
CREATE TABLE IF NOT EXISTS staging.dim_customers
(
    id BIGINT IDENTITY(1, 1),
	customer_id integer NOT NULL,
	customer_name character varying ,
	email character varying,
	registration_date timestamp without time zone
);
'''

dim_items = '''
CREATE TABLE IF NOT EXISTS staging.dim_items
(
    id BIGINT IDENTITY(1, 1),
	item_id  integer NOT NULL,
	item_name character varying,
	selling_price numeric(7,2),
	cost_price numeric(7,2)
);
'''	

dim_banks = '''
CREATE TABLE IF NOT EXISTS staging.dim_banks
(
    id BIGINT IDENTITY(1, 1),
    bank_id character varying NOT NULL,
	bank_code integer,
    bank_name character varying
);
'''		
	
dim_dates = '''
CREATE TABLE IF NOT EXISTS staging.dim_dates 
(
        id BIGINT IDENTITY(1, 1),
        date DATE,
        year int,
        month int,
        day int,
        quarter varchar,
		hour int      
);
'''		
	
ft_customer_transactions = '''
CREATE TABLE IF NOT EXISTS staging.ft_customer_transactions(
    id BIGINT IDENTITY(1, 1),
	transaction_id bigint NOT NULL ,	
	item_id bigint,
	customer_id int,
	bank_id character varying,	
	quantity int,	
	selling_price numeric(7,2),
	cost_price numeric(7,2),
	exchange_rate numeric(10,2),
	transaction_date date ,
	registration_date timestamp without time zone
);
'''

raw_data_tables = [customers, banks, items, transactions, exchange_rates]
transformed_tables = [dim_customers, dim_items,  dim_banks, dim_dates, ft_customer_transactions]
