-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

SELECT title, members.name, DATE(loan_date) AS loan_date
FROM loans 
LEFT JOIN books 
ON loans.book_id = books.id
LEFT JOIN members
ON loans.member_id = members.id;

SELECT title, loans.id AS loan_id
FROM books
LEFT JOIN loans
ON books.id = loans.book_id
GROUP BY title;


SELECT members.name, COUNT(*) AS loans
FROM members
LEFT JOIN loans
ON members.id = loans.member_id
GROUP BY members.name;

SELECT members.name, loans.id
FROM loans
RIGHT JOIN members
ON loans.member_id = members.id
ORDER BY members.name;