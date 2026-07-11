-- LeetCode 1148: Article Views I
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/article-views-i/description

SELECT distinct author_id AS id
FROM Views
WHERE author_id=viewer_id
ORDER BY author_id ASC;