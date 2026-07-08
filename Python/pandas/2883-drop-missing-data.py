# LeetCode 2883: Drop Missing Data
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/drop-missing-data/description

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])