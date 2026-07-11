-- LeetCode 1683: Invalid Tweets
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/invalid-tweets/description

SELECT TWEET_ID
FROM TWEETS
WHERE LENGTH(CONTENT)>15;