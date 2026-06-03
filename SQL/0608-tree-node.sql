-- LeetCode 608: Tree Node
-- Difficulty: Medium
-- Topic: Database
-- Link: https://leetcode.com/problems/tree-node/description/

select id,
        (case 
            when p_id is null then 'Root'
            when id not in(select distinct p_id from Tree where p_id is not null) then 'Leaf'
            else 'Inner'
        End) as type
from tree;