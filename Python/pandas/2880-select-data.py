# LeetCode 2880: Select Data
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/select-data/description/

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

# return students.query('student_id == 101')[['name', 'age']]