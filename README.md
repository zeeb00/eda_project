# Exploratory Data Analysis
> A Python package for parsing TXT/CSV files and performing Exploratory Data Analysis (EDA). It provides a CLI and Python API to quickly view data, compute mean/median, and generate plots.


## Installation

### Clone the repo
```bash
git clone https://github.com/zeeb00/eda_project.git
cd eda_project
pip install -r requirements.txt
pip install -e .
```

### From Github directly 
```
pip install "git+https://github.com/zeeb00/eda_project.git"
```

## Quick Start
After installation, you get the eda-cli command:

```
eda-cli ./examples/demo.csv \
  --summary \
  --head 5 \
  --hist a --bins 20 \
  --scatter-x a --scatter-y b \
  --outdir ./plots
```
**Arguments:**

*path → path to CSV/TXT file*

*--delimiter → field delimiter (default ,)*

*--n-rows → limit number of rows parsed*

*--no-header → specify if file has no header row*

*--head → preview N rows (default 5)*

*--summary → print mean/median stats*

*--hist <col> → generate histogram for a column*

*--scatter-x <col> --scatter-y <col> → generate scatter plot*

*--outdir → where to save plots (default plots/)*

## Python API
```
from eda_project import load_table, mean_median, plot_histogram

# Load data
df = load_table("./examples/demo.csv")

# Summary stats
print(mean_median(df))

# Plots
plot_histogram(df, "a", bins=10, savepath="plots/hist_a.png")

```
