-- Create Employees Table
CREATE TABLE Employees3 (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT
);

-- Insert Data into Employees
INSERT INTO Employees3 (first_name, last_name, department_id)
VALUES
('Rahul', 'Sharma', 101),
('Priya', 'Mehta', 102),
('Ankit', 'Verma', 103),
('Simran', 'Kaur', NULL),
('Aman', 'Singh', 101);

SELECT * FROM employees3;

-- Create Departments Table
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Insert Data into Departments
INSERT INTO Departments (department_id, department_name)
VALUES
(101, 'Sales'),
(102, 'Marketing'),
(103, 'IT'),
(104, 'HR');


SELECT * FROM Departments;

--inner join
select e.employee_id,e.first_name,e.last_name, d.department_id,d.department_name from employees3 e inner join departments d 
on e.department_id=d.department_id;

--left join
select e.employee_id,e.first_name,e.last_name, d.department_id,d.department_name from employees3 e left join departments d 
on e.department_id=d.department_id;

--right join
select e.employee_id,e.first_name,e.last_name, d.department_id,d.department_name from employees3 e right join departments d 
on e.department_id=d.department_id;