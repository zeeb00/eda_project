"""Return a 2-row DataFrame with mean and median for each numeric column."""

import pandas as pd

def mean_median(df):
    means = df.mean(numeric_only=True)
    medians = df.median(numeric_only=True)
    out = pd.concat([means, medians], axis=1).T  # transpose -> 2 rows
    out.index = ["mean", "median"]
    return out
