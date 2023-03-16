# Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true

# Solution:-



select Round(LONG_W,4)
from STATION
where LAT_N = (
select MIN(LAT_N) 
from STATION
where LAT_N > 38.7780);