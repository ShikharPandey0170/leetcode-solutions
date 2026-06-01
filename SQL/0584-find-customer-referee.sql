-- LeetCode 584: Find Customer Referee
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/find-customer-referee/description/

select name
from Customer
where referee_id!=2
or referee_id is Null;