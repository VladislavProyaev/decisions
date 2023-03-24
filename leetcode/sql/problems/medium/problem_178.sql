--url=https://leetcode.com/problems/rank-scores/description/
select score, dense_rank() over (order by score desc) as rank -- для mysql 'rank'
from scores
order by score desc;