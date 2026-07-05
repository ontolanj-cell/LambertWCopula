import matplotlib.pyplot as plt

def create_scatter_plot(df):

    plt.figure(figsize=(8,6), dpi=300)

    plt.scatter(
        df["Temperature"],
        df["Precipitation"],
        alpha=0.6,
        edgecolors="black",
        linewidth=0.3
    )

    plt.xlabel("Temperature (°C)")
    plt.ylabel("Precipitation (mm/day)")
    plt.title("Temperature vs Precipitation")

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "figures/ScatterPlot.png",
        dpi=300
    )

    plt.close()