# LeetCode 0176: Second Highest Salary
# Difficulty: Medium
# Topic: Database
# Link: https://leetcode.com/problems/second-highest-salary/description/

SELECT MAX(salary) AS SecondHighestSalary  
FROM Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee);