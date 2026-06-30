# LeetCode 2879: Display the First Three Rows
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/display-the-first-three-rows/description/

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# return employees[:3]