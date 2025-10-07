-- CREATE TABLE employee(
--     id INTEGER NOT NULL PRIMARY KEY,
--     name TEXT NOT NULL,
--     email TEXT NOT NULL UNIQUE
-- );


-- INSERT INTO employee(id, name, email)
-- VALUES
-- (6, "Musa", "musa@gmail.com"),
-- (7, "Mary", "mary@gmail.com"),
-- (8, "John", "john@gmail.com");


-- RENAME A TABLE OR COLUMN
-- ALTER TABLE employees
-- RENAME TO contractors;

-- ALTER TABLE contractors
-- RENAME COLUMN salary TO invoice;


-- ADD OR DROP A COLUMN
-- ALTER TABLE contractors
-- ADD COLUMN job_title TEXT;

-- ALTER TABLE contractors
-- DROP COLUMN is_manager;

-- ALTER TABLE employees 
-- ADD COLUMN country INTEGER;


SELECT * FROM employees;



