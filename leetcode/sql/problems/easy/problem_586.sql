--url=https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/
with cte as
         (select customer_number, COUNT(order_number) as c
          from orders
          group by customer_number)

select customer_number
from cte
where c = (select max(c) FROM cte);