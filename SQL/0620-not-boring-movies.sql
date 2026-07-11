-- LeetCode 0620: Not Boring Movies
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/not-boring-movies/description

SELECT *
FROM cinema
WHERE description != 'boring' and id % 2 != 0
ORDER BY rating DESC;