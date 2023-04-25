CREATE DATABASE customer_db;

USE customer_db;

CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_firstname VARCHAR(255) NOT NULL,
  customer_lastname VARCHAR(255) NOT NULL
);

CREATE DATABASE accounts_db;

USE accounts_db;

CREATE TABLE accounts (
  account_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT NOT NULL,
  account_type VARCHAR(255) NOT NULL,
  balance INT NOT NULL
);
