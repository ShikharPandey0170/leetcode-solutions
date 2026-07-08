# LeetCode 2887: Fill Missing Data
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/fill-missing-data/description

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products