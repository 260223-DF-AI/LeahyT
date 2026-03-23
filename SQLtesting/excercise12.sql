-- -- Create database
-- --CREATE DATABASE sql_practice;
\c chinook_pg

-- -- Create tables
-- CREATE TABLE departments (
--     dept_id SERIAL PRIMARY KEY,
--     dept_name VARCHAR(50) NOT NULL,
--     location VARCHAR(100),
--     budget DECIMAL(12, 2)
-- );

-- CREATE TABLE employees (
--     emp_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     email VARCHAR(100) UNIQUE,
--     hire_date DATE DEFAULT CURRENT_DATE,
--     salary DECIMAL(10, 2),
--     dept_id INTEGER REFERENCES departments(dept_id)
-- );

-- CREATE TABLE projects (
--     project_id SERIAL PRIMARY KEY,
--     project_name VARCHAR(100) NOT NULL,
--     start_date DATE,
--     end_date DATE,
--     budget DECIMAL(12, 2),
--     dept_id INTEGER REFERENCES departments(dept_id)
-- );

-- -- Insert sample data
-- INSERT INTO departments (dept_name, location, budget) VALUES
-- ('Engineering', 'Building A', 500000),
-- ('Sales', 'Building B', 300000),
-- ('Marketing', 'Building C', 200000),
-- ('HR', 'Building D', 150000);

-- INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id) VALUES
-- ('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
-- ('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
-- ('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
-- ('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
-- ('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
-- ('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
-- ('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
-- ('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

TRUNCATE projects 

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('extra project', '2024-12-05', '2025-06-30', 75000, 3);

-- SELECT * FROM departments;

SELECT * FROM projects;

SELECT * FROM employees WHERE email LIKE '%grace%';

SELECT * FROM departments WHERE location = 'Building A' OR location = 'Building B';

# ALTER TABLE employees ADD COLUMN TOTAL

-- SELECT dept_id, SUM(salary) FROM employees GROUP BY dept_id;

-- SELECT dept_id, COUNT(dept_id) FROM employees GROUP BY dept_id HAVING COUNT(dept_id) > 1;

-- SELECT first_name || ' ' || last_name AS full_name, 
-- dept_name, TO_CHAR(salary, '$999,999.00') AS formatted_salary FROM employees, departments;

SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT * FROM departments WHERE 2 <= (SELECT COUNT(dept_id) FROM projects);

SELECT dept_id from projects GROUP BY dept_id HAVING COUNT(*) >= 2;

SELECT COUNT(dept_id) FROM projects;

SELECT * FROM employees 