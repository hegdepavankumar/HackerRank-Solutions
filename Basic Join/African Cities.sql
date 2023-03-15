
# Author: Pavankumar Hegde

#Question :- https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true

#Answer :-

select city.name from city join country on city.countrycode = country.code where country.continent = 'Africa';