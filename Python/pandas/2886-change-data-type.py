# LeetCode 2886: Change Data Type
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/change-data-type/description

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int64')
    return students