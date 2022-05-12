CREATE TABLE products (
    id SERIAL,
    name VARCHAR(25) not null,
    PRIMARY KEY (ID)
);
CREATE TABLE clicks (
    id SERIAL,
    ts timestamp not null,
    product_id INT not null,
    PRIMARY KEY (ID),
    CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES products(id)
);
CREATE TABLE sales (
    id SERIAL,
    ts timestamp not null,
    product_id INT not null,
    price DECIMAL not null,
    PRIMARY KEY (ID),
    CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES products(id)
);
INSERT INTO products (name)
VALUES ('product A'),
    ('product B'),
    ('product C'),
    ('product D'),
    ('product E');