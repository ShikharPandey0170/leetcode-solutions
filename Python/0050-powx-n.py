# LeetCode 0050: Powx N
# Difficulty: Medium
# Topic: Math
# Link: https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        from math import pow
        return pow(x,n)
        