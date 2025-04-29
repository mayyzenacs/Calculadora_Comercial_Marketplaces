CREATE DATABASE operations ENCODING 'UTF8';
CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    percent VARCHAR(5) NOT NULL,
    valor NUMERIC NOT NULL,
    final_value NUMERIC NOT NULL,
    date_time TIMESTAMP DEFAULT now()
);