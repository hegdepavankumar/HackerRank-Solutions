# Author: Pavankumar Hegde

# Question :-  https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true

# Answer:-


select city,length(city) from station order By length(city) asc, city asc limit 1;
select distinct(City),length(city) from station order by length(city) desc, city asc limit 1;