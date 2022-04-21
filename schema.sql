CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, category TEXT, recipe TEXT, time TEXT, price TEXT);
CREATE TABLE data (id SERIAL PRIMARY KEY, recipename TEXT, creator TEXT);