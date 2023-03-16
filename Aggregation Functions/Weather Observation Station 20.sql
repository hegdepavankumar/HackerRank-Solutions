# Author: Pavankumar Hegde

# Question:- https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true

# Solution:-



SELECT Round(st.lat_n, 4)
FROM station AS st
WHERE (SELECT Count(lat_n) FROM station WHERE lat_n < st.lat_n) = (SELECT Count(lat_n) FROM station WHERE lat_n > st.lat_n);
