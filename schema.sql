CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE destinations(
    id SERIAL PRIMARY KEY,
    destination TEXT,
    price TEXT,
    duration TEXT
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    username TEXT,
    comment TEXT,
    posted TIMESTAMP
);

CREATE TABLE ratings(
    id SERIAL PRIMARY KEY,
    username TEXT,
    rating INTEGER,
    posted TIMESTAMP
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    destination TEXT
);

