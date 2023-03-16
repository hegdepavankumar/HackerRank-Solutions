# Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

# Solution:-


SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0','')))
FROM  EMPLOYEES