--DDL:
--Create, drop, alter, Truncate, comment(/*-*/), rename
--    Constrains: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT


CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    dept_head VARCHAR(50)
);
INSERT INTO departments (department_name, dept_head) VALUES
('Human Resources', 'Alice Johnson'),
('Finance', 'Robert Smith'),
('IT', 'John Doe'),
('Marketing', 'Emily Davis'),
('Sales', 'Michael Brown'),
('Customer Support', 'Sarah Wilson'),
('Research and Development', 'David Taylor'),
('Legal', 'Laura Moore'),
('Production', 'James White'),
('Logistics', 'Jessica Martin');

INSERT INTO departments (department_name, dept_head)
VALUES ('Human Resources', 'Alice Johnson');

INSERT INTO departments VALUES (NULL, 'Human Resources', 'Alice Johnson');



CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    dept_head VARCHAR(50) NOT NULL
);
--INSERT INTO department VALUES (NULL, 'Human Resources', 'Alice Johnson');   ----- Error since no Auto increment in table for PRI KEY

ALTER TABLE departments MODIFY dept_head VARCHAR(60) NOT NULL;

INSERT INTO departments
VALUES (1, 'Human Resources', 'Alice Johnson');

ALTER TABLE departments MODIFY department_id INT NOT NULL AUTO_INCREMENT;


ALTER TABLE departments CHANGE dept_head department_head VARCHAR(50) NOT NULL;
ALTER TABLE departments ADD CONSTRAINT unique_department_name UNIQUE (department_name);
--ALTER TABLE employees ADD CONSTRAINT check_salary CHECK (salary > 0);
TRUNCATE TABLE departments;

RENAME TABLE departments TO dept_info;

ALTER TABLE dept_info RENAME TO dept_data;


CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    hire_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    department_id INT
);


INSERT INTO employees (employee_id, first_name, last_name, email, salary, hire_date, department_id) VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', 75000.00, DEFAULT, 1),
(2, 'Bob', 'Smith', 'bob.smith@example.com', 65000.00, DEFAULT, 2),
(3, 'Charlie', 'Brown', 'charlie.brown@example.com', 80000.00, DEFAULT, 3),
(4, 'Diana', 'Prince', 'diana.prince@example.com', 90000.00, DEFAULT, 4),
(5, 'Ethan', 'Hunt', 'ethan.hunt@example.com', 85000.00, DEFAULT, 5),
(6, 'Fiona', 'Clark', 'fiona.clark@example.com', 70000.00, DEFAULT, 1),
(7, 'George', 'Wilson', 'george.wilson@example.com', 72000.00, DEFAULT, 2),
(8, 'Hannah', 'Davis', 'hannah.davis@example.com', 81000.00, DEFAULT, 3),
(9, 'Ian', 'Wright', 'ian.wright@example.com', 64000.00, DEFAULT, 4),
(10, 'Julia', 'Stone', 'julia.stone@example.com', 69000.00, DEFAULT, 5),
(11, 'Kevin', 'Hart', 'kevin.hart@example.com', 74000.00, DEFAULT, 1),
(12, 'Laura', 'Moore', 'laura.moore@example.com', 76000.00, DEFAULT, 2),
(13, 'Michael', 'Brown', 'michael.brown@example.com', 83000.00, DEFAULT, 3),
(14, 'Natalie', 'Taylor', 'natalie.taylor@example.com', 92000.00, DEFAULT, 4),
(15, 'Oscar', 'Miller', 'oscar.miller@example.com', 88000.00, DEFAULT, 5),
(16, 'Paula', 'Green', 'paula.green@example.com', 71000.00, DEFAULT, 1),
(17, 'Quentin', 'Blake', 'quentin.blake@example.com', 73000.00, DEFAULT, 2),
(18, 'Rachel', 'Adams', 'rachel.adams@example.com', 79000.00, DEFAULT, 3),
(19, 'Steven', 'King', 'steven.king@example.com', 86000.00, DEFAULT, 4),
(20, 'Tina', 'White', 'tina.white@example.com', 67000.00, DEFAULT, 5);


INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id) VALUES (21, 'Alice', 'Johnson', 'alice.johnson@example.com', 75000.00, 1);


UPDATE employees SET department_id = 4 WHERE employee_id = 3;

DELETE FROM employees WHERE employee_id = 3;




--skill
--id, skill
--1 python
--2 sql
--3 django
--4 react
--
--
--teachers
--id, name
--1 nithin
--2 sanjay
--
--
--students
--id, name, skill_id, teachers_id
--1 venkey 1 2
--2 purnesh 2 2
--3 usha 3 1
--4 kiran 4 2


CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,     -- Primary Key
    first_name VARCHAR(50) NOT NULL,                -- NOT NULL Constraint
    last_name VARCHAR(50) NOT NULL,                 -- NOT NULL Constraint
    email VARCHAR(100) UNIQUE NOT NULL,             -- UNIQUE and NOT NULL Constraint
    phone_number VARCHAR(15) UNIQUE,                -- UNIQUE Constraint
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP   -- DEFAULT Constraint
);


CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,     -- Primary Key
    product_name VARCHAR(100) NOT NULL,            -- NOT NULL Constraint
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0), -- NOT NULL and CHECK Constraint
    stock_quantity INT CHECK (stock_quantity >= 0) -- CHECK Constraint
);



CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,        -- Primary Key
    customer_id INT NOT NULL,                       -- Foreign Key (references customers)
    product_id INT NOT NULL,                        -- Foreign Key (references products)
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,  -- DEFAULT Constraint
    quantity INT NOT NULL CHECK (quantity > 0),     -- CHECK Constraint
    total_price DECIMAL(10, 2) NOT NULL,            -- NOT NULL Constraint
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), -- FK Constraint
    FOREIGN KEY (product_id) REFERENCES products(product_id)     -- FK Constraint
);



INSERT INTO customers (customer_id, first_name, last_name, email, phone_number) VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', '1234567890'),
(2, 'Bob', 'Smith', 'bob.smith@example.com', '1234567891'),
(3, 'Charlie', 'Brown', 'charlie.brown@example.com', '1234567892'),
(4, 'Diana', 'Prince', 'diana.prince@example.com', '1234567893'),
(5, 'Ethan', 'Hunt', 'ethan.hunt@example.com', '1234567894'),
(6, 'Fiona', 'Clark', 'fiona.clark@example.com', '1234567895'),
(7, 'George', 'Wilson', 'george.wilson@example.com', '1234567896'),
(8, 'Hannah', 'Davis', 'hannah.davis@example.com', '1234567897'),
(9, 'Ian', 'Wright', 'ian.wright@example.com', '1234567898'),
(10, 'Julia', 'Stone', 'julia.stone@example.com', '1234567899');



INSERT INTO products (product_id, product_name, price, stock_quantity) VALUES
(101, 'Laptop', 1200.00, 50),
(102, 'Smartphone', 800.00, 100),
(103, 'Tablet', 400.00, 75),
(104, 'Headphones', 150.00, 200),
(105, 'Smartwatch', 250.00, 150);




INSERT INTO orders (order_id, customer_id, product_id, quantity, total_price) VALUES
(1001, 1, 101, 1, 1200.00),
(1002, 2, 102, 2, 1600.00),
(1003, 3, 103, 3, 1200.00),
(1004, 4, 104, 1, 150.00),
(1005, 5, 105, 2, 500.00),
(1006, 6, 101, 1, 1200.00),
(1007, 7, 102, 1, 800.00),
(1008, 8, 103, 4, 1600.00),
(1009, 9, 104, 2, 300.00),
(1010, 10, 105, 3, 750.00),
(1011, 1, 102, 1, 800.00),
(1012, 2, 103, 2, 800.00),
(1013, 3, 104, 3, 450.00),
(1014, 4, 105, 1, 250.00),
(1015, 5, 101, 1, 1200.00),
(1016, 6, 102, 3, 2400.00),
(1017, 7, 103, 1, 400.00),
(1018, 8, 104, 2, 300.00),
(1019, 9, 105, 1, 250.00),
(1020, 10, 101, 2, 2400.00),
(1021, 1, 104, 3, 450.00),
(1022, 2, 105, 2, 500.00),
(1023, 3, 103, 4, 1600.00),
(1024, 4, 102, 1, 800.00),
(1025, 5, 101, 2, 2400.00),
(1026, 6, 105, 1, 250.00),
(1027, 7, 103, 3, 1200.00),
(1028, 8, 104, 1, 150.00),
(1029, 9, 102, 2, 1600.00),
(1030, 10, 101, 1, 1200.00);





select * from orders;

select customer_id, product_id, quantity, total_price from orders;

select * from orders where product_id=101;

select customer_id, product_id, quantity, total_price from orders where product_id=101;

select * from orders inner join products on orders.product_id=products.product_id where orders.product_id=101;










-- world

select * from country; -- full select
select code, name, capital from country; -- select column in table
select code, name, capital from country where code='ABW';
select * from city;
select name, CountryCode, District, Population from city;
select name, CountryCode, District, Population from city where CountryCode='NLD' and District='Zuid-Holland' and Population>=440900;  -- filter by where condition
select name, CountryCode, District, Population from city where CountryCode='NLD' order by CountryCode desc; -- order by desc
select name, CountryCode, District, Population from city where CountryCode='NLD' order by name asc;  -- order by asc
select CountryCode, District, name, Population from city order by CountryCode, District, name asc;  -- multiple column ordering or sorting

select count(*) from city where CountryCode='NLD'; -- and District='Zuid-Holland';
select * from city where CountryCode='NLD'; --  and District='Zuid-Holland';

select CountryCode, name, max(Population) from city group by CountryCode, name;
select CountryCode, name, min(Population) from city group by CountryCode, name;

select CountryCode, District, avg(Population) from city group by CountryCode, District;
select CountryCode, avg(Population) from city group by CountryCode;

select sum(Population) from city where CountryCode='NLD';



select * from city limit 5;
select * from country limit 5;
select * from countrylanguage limit 5;
select ct.ID, ct.Name, ct.CountryCode,co.Name as 'Country Name',  ct.District, ct.Population, co.IndepYear from city as ct inner join country as co on ct.CountryCode=co.Code;


select ct.ID, ct.Name, ct.CountryCode,co.Name as 'Country Name',  ct.District, ct.Population, co.IndepYear from city as ct left join country as co on ct.CountryCode=co.Code;
select ct.ID, ct.Name, ct.CountryCode,co.Name as 'Country Name',  ct.District, ct.Population, co.IndepYear from city as ct right join country as co on ct.CountryCode=co.Code;















CREATE TABLE students (
    id INT ,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    grade_level INT NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE marks (
    mark_id INT ,
    student_id INT NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    marks_obtained INT CHECK (marks_obtained BETWEEN 0 AND 100),
    exam_date DATE,
    academic_year YEAR NOT NULL
);


INSERT INTO students (id, first_name, last_name, email, date_of_birth, grade_level, enrollment_date)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '2005-03-15', 10, '2024-08-01'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '2006-07-22', 9, '2024-08-01'),
(3, 'Mike', 'Johnson', 'mike.johnson@example.com', '2007-11-10', 8, '2023-08-01'),
(4, 'Emily', 'Brown', 'emily.brown@example.com', '2005-12-05', 10, '2024-08-01'),
(5, 'Chris', 'Davis', 'chris.davis@example.com', '2004-05-25', 11, '2024-08-01');



INSERT INTO marks (mark_id, student_id, subject_name, marks_obtained, exam_date, academic_year)
VALUES
(1, 1, 'Mathematics', 30, '2024-01-10', 2024),
(2, 2, 'Science', 45, '2024-01-12', 2024),
(3, 3, 'English', 60, '2024-01-14', 2024),
(4, 4, 'Mathematics', 70, '2023-12-15', 2023),
(5, 5, 'History', 85, '2024-01-10', 2024),
(6, 1, 'Science', 50, '2023-11-20', 2023),
(7, 2, 'English', 35, '2023-11-22', 2023),
(8, 3, 'History', 70, '2023-12-01', 2023),
(9, 4, 'Mathematics', 45, '2023-11-25', 2023),
(10, 5, 'English', 90, '2023-12-01', 2023),
(11, 1, 'Mathematics', 60, '2022-05-15', 2022),
(12, 2, 'Science', 55, '2022-06-10', 2022),
(13, 3, 'English', 65, '2022-06-20', 2022),
(14, 4, 'History', 50, '2022-07-05', 2022),
(15, 5, 'Science', 75, '2022-07-10', 2022),
(16, 1, 'English', 40, '2023-03-15', 2023),
(17, 2, 'History', 60, '2023-03-18', 2023),
(18, 3, 'Science', 80, '2023-03-20', 2023),
(19, 4, 'Mathematics', 30, '2023-04-10', 2023),
(20, 5, 'Mathematics', 70, '2024-01-18', 2024);




SELECT
    mark_id,
    student_id,
    subject_name,
    marks_obtained,
    exam_date,
    academic_year,
    CASE
        WHEN marks_obtained >= 80 THEN 'A'
        WHEN marks_obtained >= 70 THEN 'B'
        WHEN marks_obtained >= 60 THEN 'C'
        WHEN marks_obtained >= 50 THEN 'D'
        WHEN marks_obtained >= 30 THEN 'F'
        ELSE 'Invalid'
    END AS grade
FROM marks;

























select * from students order by id;

select * from marks order by mark_id;

select * from students as st inner join marks as mk on st.id=mk.student_id order by id;
select * from students as st left join marks as mk on st.id=mk.student_id order by id;
select st.id, mk.student_id, st.grade_level, mk.subject_name, mk.marks_obtained from students as st right join marks as mk on st.id=mk.student_id order by id;



select
subject_name,
marks_obtained,
case
	when marks_obtained >= 80 then "A"
    when marks_obtained >= 60 then "B"
    when marks_obtained >= 35 then "c"
    else "Fail"
end as grade
from marks;









select * from marks where subject_name like '%s';
select * from students where last_name like 'D%';
select * from students where last_name like '%n';
select * from students where last_name like '%o%';
select * from students where last_name like 'joh%o%';

-- select * from students where last_name like '_oe';
-- select * from students where last_name like '__ith';
-- select * from students where last_name like '__i%';
-- select * from students where last_name like '[D]%';





















