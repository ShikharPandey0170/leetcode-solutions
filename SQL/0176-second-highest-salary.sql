-- LeetCode 176: Second Highest Salary
-- Difficulty: Medium
-- Topic: Database
-- Link: https://leetcode.com/problems/second-highest-salary/description/

SELECT max(salary) 
AS SecondHighestSalary  
FROM Employee 
WHERE salary<(SELECT max(salary) FROM Employee);