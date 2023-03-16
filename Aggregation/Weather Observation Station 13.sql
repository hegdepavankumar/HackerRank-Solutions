# Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true

# Solution:-


select Round(sum(LAT_N),4)
from STATION 
where LAT_N > 38.7880 and LAT_N < 137.2345;