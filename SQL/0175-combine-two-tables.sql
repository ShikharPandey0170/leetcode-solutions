-- LeetCode 175: Combine Two Tables
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/combine-two-tables/description/

SELECT p.firstName,p.lastName,a.city,a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;