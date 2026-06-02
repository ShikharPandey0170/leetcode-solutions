-- LeetCode 607: Sales Person
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/sales-person/description/

select s.name
from SalesPerson s
where s.sales_id not in(
    select o.sales_id
    from orders o
    join company c
    on o.com_id=c.com_id
    where c.name='RED'
);