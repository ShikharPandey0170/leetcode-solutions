-- LeetCode 182: Duplicate Emails
-- Difficulty: Easy
-- Topic: Database
-- Link: https://leetcode.com/problems/duplicate-emails/description/

select email as Email
from person
group by email
having count(email)>1;