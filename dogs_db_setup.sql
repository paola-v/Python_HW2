USE dogs_db;
CREATE TABLE dogs(
id INTEGER AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
breed VARCHAR(100),
color VARCHAR(100),
age INT,
mood ENUM('playful','excited','relaxed','fearful'),
sex ENUM('girl','boy')
);

CREATE TABLE owners(
id INTEGER PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
phone VARCHAR(100),
email VARCHAR(100),
dog_id INT
);

SELECT * FROM dogs;

SELECT * FROM owners;


