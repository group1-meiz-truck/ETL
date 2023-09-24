dim_customers = '''
INSERT INTO staging.dim_customers(
customer_id,
customer_name,
email,
registration_date)
SELECT id, name, email, registered_at
FROM raw_data.customers; 

'''


dim_items= '''
INSERT INTO staging.dim_items(
item_id,
item_name,
selling_price,
cost_price)
SELECT id,name,selling_price, cost_price
FROM raw_data.items;

'''

dim_banks = '''
INSERT INTO staging.dim_banks(
bank_id,
bank_code,
bank_name)
SELECT * FROM raw_data.banks;

'''

dim_dates = '''
INSERT INTO staging.dim_dates(
date,
year,
month,
day,
quarter,
hour	
)
SELECT registered_at date, EXTRACT(YEAR FROM registered_at) year_, EXTRACT(MONTH FROM registered_at) month_, 
EXTRACT(DAY FROM registered_at) day_, EXTRACT(QUARTER FROM registered_at) quarter_,
EXTRACT(HOUR FROM registered_at) hour_
FROM customers;

'''

ft_customer_transactions = '''

INSERT INTO staging.ft_customer_transactions(
transaction_id,	
item_id,
customer_id,
bank_id,	
quantity,	
selling_price,
cost_price,
exchange_rate,
transaction_date,
registration_date)

SELECT DISTINCT t.id, t.item_id,t.customer_id,t.bank_id, t.qty,
i.selling_price, i.cost_price, e.rate,t.date,c.registered_at
FROM raw_data.transactions t 
JOIN raw_data.items i ON t.item_id = i.id
JOIN raw_data.exchange_rates e ON t.bank_id = e.bank_id
JOIN raw_data.customers c ON t.customer_id = c.id

'''

transformation_queries = [dim_customers, dim_items, dim_banks,dim_dates,ft_customer_transactions ]