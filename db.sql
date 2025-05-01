CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    choice VARCHAR(5) NOT NULL,
    valor NUMERIC NOT NULL,
    final_value NUMERIC NOT NULL,
    date_time TIMESTAMP DEFAULT now()
);