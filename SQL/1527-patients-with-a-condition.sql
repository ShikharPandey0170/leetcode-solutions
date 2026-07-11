-- LeetCode 1527: Patients With a Condition
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/patients-with-a-condition/description

SELECT *
FROM patients
WHERE conditions LIKE 'DIAB1%' 
OR conditions LIKE '% DIAB1%'