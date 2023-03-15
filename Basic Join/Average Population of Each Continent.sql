# Author: Pavankumar Hegde

#Question :- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true

#Answer :-

select country.continent, floor(avg(city.population)) from country join city on city.countrycode = country.code group by country.continent;