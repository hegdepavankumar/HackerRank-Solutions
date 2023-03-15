# Author: Pavankumar Hegde

# Question :-  https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true

# Answer:-


select count(city) - count(distinct city) from station;
