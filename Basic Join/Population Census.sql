# Author: Pavankumar Hegde

#Question :- https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true

#Answer :-

select sum(city.population) from country left join city on country.code = city.countrycode where country.continent = 'Asia'