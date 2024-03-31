CREATE TABLE rental_properties (
    id SERIAL PRIMARY KEY,
    description VARCHAR,
    house_type VARCHAR,
    price FLOAT,
    area FLOAT,
    location VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
