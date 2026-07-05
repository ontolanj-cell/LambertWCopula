import pandas as pd
from scipy.stats import rankdata

def create_pseudo_observations(df):

    n = len(df)

    U = rankdata(
        df["Temperature"],
        method="average"
    )/(n+1)

    V = rankdata(
        df["Precipitation"],
        method="average"
    )/(n+1)

    pseudo = pd.DataFrame({

        "U": U,

        "V": V

    })

    pseudo.to_excel(

        "results/PseudoObservations.xlsx",

        index=False

    )

    return pseudo