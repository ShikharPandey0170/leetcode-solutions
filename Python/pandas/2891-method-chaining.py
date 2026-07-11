# LeetCode 2891: Method Chaining
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/method-chaining/description/

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight']>100].sort_values('weight', ascending=False)[['name']]