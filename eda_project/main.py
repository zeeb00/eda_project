import argparse
from pathlib import Path
from eda_project.parser import load_table
from eda_project.eda_toolkit import mean_median
from eda_project.plots import plot_histogram, plot_scatter

def main():
    parser = argparse.ArgumentParser(description="Simple EDA: parse, summarize, and plot")
    parser.add_argument("path", help="Path to CSV/TXT file")
    parser.add_argument("--delimiter", default=",", help="Field delimiter (default: ,)") # for tab --delimiter "`t" , # for single space --delimiter " " 
    parser.add_argument("--n-rows", type=int, default=None, help="Limit rows parsed")
    parser.add_argument("--no-header", action="store_true", help="File has no header row")
    parser.add_argument("--head", type=int, default=5, help="Preview N rows")

    # EDA
    parser.add_argument("--summary", action="store_true", help="Print mean/median table")

    # Plots
    parser.add_argument("--hist", help="Column for histogram")
    parser.add_argument("--bins", type=int, default=30)
    parser.add_argument("--scatter-x", help="X column for scatter")
    parser.add_argument("--scatter-y", help="Y column for scatter")
    parser.add_argument("--outdir", default="plots", help="Directory to save plots")

    args = parser.parse_args()

    df = load_table(
        args.path,
        delimiter=args.delimiter,
        n_rows=args.n_rows,
        has_header=not args.no_header,
    )

    print("\nHead:\n", df.head(args.head))

    if args.summary:
        print("\nMean/Median (numeric columns):\n", mean_median(df))

    outdir = Path(args.outdir)
    if args.hist:
        out = outdir / ("hist_" + args.hist + ".png")
        plot_histogram(df, args.hist, bins=args.bins, savepath=out)
        print("Saved histogram →", out)

    if args.scatter_x and args.scatter_y:
        out = outdir / ("scatter_" + args.scatter_y + "_vs_" + args.scatter_x + ".png")
        plot_scatter(df, args.scatter_x, args.scatter_y, savepath=out)
        print("Saved scatter →", out)


if __name__ == "__main__":
    main()
