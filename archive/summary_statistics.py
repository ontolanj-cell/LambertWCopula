import pandas as pd

def summary_statistics(df):

    summary = df.describe()

    print("\nSummary Statistics")

    print(summary)

    summary.to_excel(
        "results/SummaryStatistics.xlsx"
    )