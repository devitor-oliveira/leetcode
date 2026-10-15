create table customers (
  id SERIAL PRIMARY KEY,
  name varchar,
  street varchar,
  city varchar,
  state char,
  credit_limit number
);
INSERT INTO customers (name, street, city, state, credit_limit)
VALUES (
    "Pedro",
    "Rua CArlos",
    "Porto Alegre",
    "RS",
    700,
    00
  ),
  (
    "Antonio",
    "Rua CArlos",
    "Belo Horizonte",
    "MG",
    3500,
    00
  );