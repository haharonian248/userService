DROP TABLE IF EXISTS poll_user;

CREATE TABLE poll_user (
    id int(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(300) NOT NULL DEFAULT '',
    last_name VARCHAR(300) NOT NULL DEFAULT '',
    email VARCHAR(300) NOT NULL DEFAULT '',
    age int(3),
    address VARCHAR(300) NOT NULL DEFAULT '',
    joining_date DATE NOT NULL DEFAULT '2000-01-01',
    is_registered BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id)
);

INSERT INTO poll_user (first_name, last_name, email, age, address, joining_date, is_registered)
VALUES
('Alice', 'Green', 'alice@example.com', 28, '123 Maple St', '2024-01-10', FALSE),
('Bob', 'Smith', 'bob@example.com', 34, '45 Oak Ave', '2024-02-15', TRUE),
('Charlie', 'Brown', 'charlie@example.com', 22, '78 Pine Rd', '2024-03-01', FALSE),
('Diana', 'White', 'diana@example.com', 30, '90 Cedar Blvd', '2024-01-20', TRUE),
('Ethan', 'Black', 'ethan@example.com', 27, '12 Birch Ln', '2024-02-05', FALSE);