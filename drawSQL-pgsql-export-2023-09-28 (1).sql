CREATE TABLE "dim_customers"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" TEXT NOT NULL,
    "registration_date" DATE NOT NULL
);
ALTER TABLE
    "dim_customers" ADD PRIMARY KEY("id");
CREATE TABLE "dim_dates"(
    "date" DATE NOT NULL,
    "month" INTEGER NOT NULL,
    "year" INTEGER NOT NULL,
    "quarter" INTEGER NOT NULL,
    "hour" INTEGER NOT NULL,
    "day" INTEGER NOT NULL
);
ALTER TABLE
    "dim_dates" ADD PRIMARY KEY("date");
CREATE TABLE "dim_banks"(
    "bank_id" VARCHAR(255) NOT NULL,
    "bank_code" BIGINT NOT NULL,
    "bank_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "dim_banks" ADD PRIMARY KEY("bank_id");
CREATE TABLE "dim_items"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "selling_price" DOUBLE PRECISION NOT NULL,
    "cost_price" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "dim_items" ADD PRIMARY KEY("id");
CREATE TABLE "ft_customer_transactions"(
    "item_id" BIGINT NOT NULL,
    "customer_id" BIGINT NOT NULL,
    "bank_id" VARCHAR(255) NOT NULL,
    "selling_price" DOUBLE PRECISION NOT NULL,
    "cost_price" DOUBLE PRECISION NOT NULL,
    "quantity" BIGINT NOT NULL,
    "exchange_rate" BIGINT NOT NULL,
    "transaction_date" DATE NOT NULL,
    "registration_date" DATE NOT NULL
);
ALTER TABLE
    "ft_customer_transactions" ADD PRIMARY KEY("item_id");
ALTER TABLE
    "ft_customer_transactions" ADD CONSTRAINT "ft_customer_transactions_item_id_foreign" FOREIGN KEY("item_id") REFERENCES "dim_items"("id");
ALTER TABLE
    "ft_customer_transactions" ADD CONSTRAINT "ft_customer_transactions_registration_date_foreign" FOREIGN KEY("registration_date") REFERENCES "dim_dates"("date");
ALTER TABLE
    "ft_customer_transactions" ADD CONSTRAINT "ft_customer_transactions_customer_id_foreign" FOREIGN KEY("customer_id") REFERENCES "dim_customers"("id");
ALTER TABLE
    "ft_customer_transactions" ADD CONSTRAINT "ft_customer_transactions_bank_id_foreign" FOREIGN KEY("bank_id") REFERENCES "dim_banks"("bank_id");