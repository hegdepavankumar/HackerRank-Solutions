# Author: Pavankumar Hegde

# Question :-  https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true

# Answer:-

select distinct city from station where right(city,1) in('a','e','i','o','u')
