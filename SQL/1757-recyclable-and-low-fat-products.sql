-- LeetCode 1757: Recyclable and Low Fat Products
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/recyclable-and-low-fat-products/description

SELECT product_id 
FROM Products 
WHERE low_fats='Y' 
    AND recyclable='Y';