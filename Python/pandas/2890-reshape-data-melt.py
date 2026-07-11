# LeetCode 2890: Reshape Data: Melt
# Difficulty: Easy
# Topic: pandas
# Link: https://leetcode.com/problems/reshape-data-melt/description

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars='product', value_name='sales', var_name='quarter')