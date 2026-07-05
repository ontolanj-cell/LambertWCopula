import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau

def correlation_analysis(df):

    pearson = pearsonr(

        df["Temperature"],

        df["Precipitation"]

    )

    spearman = spearmanr(

        df["Temperature"],

        df["Precipitation"]

    )

    kendall = kendalltau(

        df["Temperature"],

        df["Precipitation"]

    )

    table = pd.DataFrame({

        "Measure":[

            "Pearson",

            "Spearman",

            "Kendall"

        ],

        "Coefficient":[

            pearson.statistic,

            spearman.statistic,

            kendall.statistic

        ],

        "p-value":[

            pearson.pvalue,

            spearman.pvalue,

            kendall.pvalue

        ]

    })

    table.to_excel(

        "results/CorrelationMatrix.xlsx",

        index=False

    )

    print(table)