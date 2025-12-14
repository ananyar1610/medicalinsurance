import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_histogram(df: pd.DataFrame, column: str, title: str):
    plt.title(title)
    sns.histplot(x=column, data=df)
    plt.show()


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue=None):
    sns.scatterplot(x=x, y=y, hue=hue, data=df)
    plt.show()


def plot_box(df: pd.DataFrame, x=None, y=None):
    sns.boxplot(x=x, y=y, data=df)
    plt.show()
