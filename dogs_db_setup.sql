USE dogs_db;


# Drop tables if they exist
DROP TABLE IF EXISTS DOGS;
DROP TABLE IF EXISTS OWNERS;


# Create tables to match db models in main.py
CREATE TABLE IF NOT EXISTS dogs(
id INTEGER AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
breed VARCHAR(100),
color VARCHAR(100),
age INT,
mood ENUM('playful','excited','relaxed','fearful'),
sex ENUM('girl','boy')
);

CREATE TABLE IF NOT EXISTS owners(
id INTEGER PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
phone VARCHAR(100),
email VARCHAR(100),
dog_id INT,
FOREIGN KEY (dog_id) REFERENCES dogs(id)
);


# Check to make sure the tables were created 
SELECT * FROM dogs;

SELECT * FROM owners;


