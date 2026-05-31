-- LeetCode 511: Game Play Analysis I
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/game-play-analysis-i/

select player_id,min(event_date) as first_login
from activity
group by player_id;