# Author: Pavankumar Hegde

# Question :-  https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true

# Answer:-


select distinct city from station where left(city,1) not in('a','e','i','o','u') or right(city,1) not in('a','e','i','o','u');
