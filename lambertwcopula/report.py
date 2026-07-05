"""
Automatic report generation for Lambert W Copula.
"""

from pathlib import Path
import json
import csv


# ==========================================================
# Text Report
# ==========================================================

def save_text_report(results, filename="reports/results.txt"):
    """
    Save a formatted text report.
    """

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as f:

        for key, value in results.items():

            f.write(f"{key:25s}: {value}\n")


# ==========================================================
# JSON Report
# ==========================================================

def save_json(results, filename="reports/results.json"):
    """
    Save results as JSON.
    """

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            results,
            f,
            indent=4,
        )


# ==========================================================
# CSV Report
# ==========================================================

def save_csv(results, filename="reports/results.csv"):
    """
    Save results as CSV.
    """

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:

        writer = csv.writer(f)

        writer.writerow(["Metric", "Value"])

        for key, value in results.items():

            writer.writerow([key, value])