-- LeetCode 183: Customers Who Never Order
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/customers-who-never-order/

select name as Customers
from customers
where id NOT IN(select customerID from orders)