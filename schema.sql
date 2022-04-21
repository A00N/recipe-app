CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, category TEXT, recipe TEXT, time TEXT, price TEXT);
CREATE TABLE data (id SERIAL PRIMARY KEY, recipename TEXT, creator TEXT);
CREATE TABLE categories (id SERIAL PRIMARY KEY, category TEXT);
CREATE TABLE times (id SERIAL PRIMARY KEY, time TEXT);
CREATE TABLE prices (id SERIAL PRIMARY KEY, price TEXT);