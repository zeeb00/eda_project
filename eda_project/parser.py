"""Load a simple CSV/TXT file assuming each column is a parameter.
- Default delimiter is comma. Override with `delimiter` (e.g., "\t" for tab).
- Set `has_header=False` if the first row is data.
"""

import pandas as pd

def load_table(path, delimiter=",", n_rows=None, has_header=True):

    header = 0 if has_header else None
    df = pd.read_csv(path, sep=delimiter, nrows=n_rows, header=header)
    if not has_header:
        df.columns = ["col_" + str(i + 1) for i in range(len(df.columns))]
    return df
