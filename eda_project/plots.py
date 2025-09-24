from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def _ensure_numeric_inplace(df, column):
    if not pd.api.types.is_numeric_dtype(df[column]):
        df[column] = pd.to_numeric(df[column], errors="coerce")


def plot_histogram(df, column, bins=30, savepath=None, show=False):
    _ensure_numeric_inplace(df, column)
    fig, ax = plt.subplots()
    ax.hist(df[column].dropna(), bins=bins)
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram: " + column)
    fig.tight_layout()

    if savepath:
        savepath = Path(savepath)
        savepath.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(savepath, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig, ax


def plot_scatter(df, x, y, savepath=None, show=False):
    _ensure_numeric_inplace(df, x)
    _ensure_numeric_inplace(df, y)
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title("Scatter: {} vs {}".format(y, x))
    fig.tight_layout()

    if savepath:
        savepath = Path(savepath)
        savepath.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(savepath, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig, ax
