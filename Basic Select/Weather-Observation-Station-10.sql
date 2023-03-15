# Author: Pavankumar Hegde

# Question :-  https://www.hackerrank.com/challenges/weather-observation-station-10/problem?isFullScreen=true

# Answer:-


select distinct(city) from station where
city not like "%a" and
city not like "%e" and
city not like "%i" and
city not like "%o" and
city not like "%u";

