--url=https://leetcode.com/problems/human-traffic-of-stadium/description/
SELECT DISTINCT t1.*
FROM stadium t1,
     stadium t2,
     stadium t3
WHERE t1.people >= 100
  AND t2.people >= 100
  AND t3.people >= 100
  AND (
        (t1.id - t2.id = 1 and t1.id - t3.id = 2 and t2.id - t3.id = 1)
        OR (t2.id - t1.id = 1 and t2.id - t3.id = 2 and t1.id - t3.id = 1)
        OR (t3.id - t2.id = 1 and t2.id - t1.id = 1 and t3.id - t1.id = 2)
    )
ORDER BY t1.id;