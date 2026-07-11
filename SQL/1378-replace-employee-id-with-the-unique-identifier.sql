-- LeetCode 1378: Replace Employee ID With Unique Identifier
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/replace-employee-id-with-unique-identifier/description

SELECT EU.unique_id, E.name
FROM Employees E
LEFT JOIN EmployeeUNI EU ON E.id=EU.id;