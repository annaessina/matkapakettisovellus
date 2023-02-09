CREATE TABLE destinations (
     id SERIAL PRIMARY KEY,
     destination TEXT,
     price INTEGER,
     duration INTEGER,
);

CREATE TABLE  users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
);

CREATE TABLE orders (
     id SERIAL PRIMARY KEY,
     order TEXT,
     date  INTEGER,
);
