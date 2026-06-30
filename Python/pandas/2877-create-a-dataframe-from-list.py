# LeetCode 2877: Create a DataFrame from list
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/create-a-dataframe-from-list/description/

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data)
    df.columns = ["student_id", "age"]
    return df

# return pd.DataFrame(student_data, columns = ["student_id", "age"])