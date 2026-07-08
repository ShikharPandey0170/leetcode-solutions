# LeetCode 2882: Drop Duplicate Rows
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/drop-duplicate-rows/description

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'],keep='first')