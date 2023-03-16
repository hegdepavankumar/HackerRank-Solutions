# Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true

# Solution:-


SELECT MONTHS*SALARY AS earnings, COUNT(*)
FROM employee
GROUP BY earnings 
ORDER BY earnings DESC
LIMIT 1;