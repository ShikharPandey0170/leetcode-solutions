# LeetCode 2885: Rename Columns
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/rename-columns/description

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
    return students    