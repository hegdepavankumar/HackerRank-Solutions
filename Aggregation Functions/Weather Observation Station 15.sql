 # Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true

# Solution:-

 
 select Round(LONG_W,4)
 from  STATION
 where LAT_N = (Select Max(LAT_N)from STATION where LAT_N < 137.2345);