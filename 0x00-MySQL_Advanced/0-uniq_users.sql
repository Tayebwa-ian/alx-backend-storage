-- creates a table users on any Database
CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT NOT NULL,
       email VARCHAR(255) UNIQUE NOT NULL,
       name VARCHAR(255),
       PRIMARY KEY (ID)
);
