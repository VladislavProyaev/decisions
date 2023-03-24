--url=https://leetcode.com/problems/sales-analysis-iii/description/
select p.product_id, product_name from sales
join product p on sales.product_id = p.product_id
group by p.product_id, product_name
having min(sale_date) >= '2019-01-01' AND max(sale_date) <= '2019-03-31';