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