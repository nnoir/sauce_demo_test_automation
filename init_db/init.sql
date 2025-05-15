CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS test_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO test_users (username, password)
VALUES
('standard_user', 'secret_sauce'),
('locked_out_user', 'secret_sauce'),
('problem_user', 'secret_sauce'),
('performance_glitch_user', 'secret_sauce'),
('error_user', 'secret_sauce'),
('visual_user', 'secret_sauce');