CREATE DATABASE IF NOT EXISTS register;

USE register;

CREATE TABLE users(
username varchar(255) unique,
password varchar(255),
created_at datetime
);