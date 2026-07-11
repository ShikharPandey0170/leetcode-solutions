# LeetCode 2889: Reshape Data: Pivot
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/reshape-data-pivot/description

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')