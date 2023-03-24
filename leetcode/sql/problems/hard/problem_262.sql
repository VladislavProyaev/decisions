--url=https://leetcode.com/problems/trips-and-users/description/
with counted as (SELECT request_at as            Day,
                        COUNT(*)                 a,
                        COUNT(CASE
                                  WHEN status = 'cancelled_by_driver' OR
                                       status = 'cancelled_by_client' THEN 1
                                  ELSE NULL END) b
                 FROM trips t
                          JOIN
                      Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
                          JOIN
                      Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
                 WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
                 GROUP BY request_at)

select counted.Day,
       round(cast(counted.b as decimal) / cast(counted.a as decimal),
             2) Cancellation_Rate --в MySQL 'Cancellation Rate'
from counted;
