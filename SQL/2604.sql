CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    amount numeric,
    price numeric
);

insert into
    products (name, amount, price)
VALUES ('wardrobe', 100, 80),
    ('table', 1000, 560);

SELECT id, name FROM products WHERE "price" < 10 OR "price" > 100;