"""
HTML Report Generator
=====================
"""

from pathlib import Path


def generate_html(results, figures, filename):
    """
    Generate an HTML report.
    """

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>Lambert W Copula Report</title>

<style>

body {{

    font-family: Arial;

    margin:40px;

    line-height:1.6;

}}

h1{{color:#003366;}}

h2{{color:#005588;}}

table{{
border-collapse:collapse;
width:70%;
}}

td,th{{
border:1px solid #ccc;
padding:8px;
}}

th{{
background:#efefef;
}}

img{{
width:700px;
margin-top:15px;
margin-bottom:30px;
border:1px solid #ddd;
}}

</style>

</head>

<body>

<h1>Lambert W Copula Analysis Report</h1>

<h2>Model Summary</h2>

<table>

<tr><th>Metric</th><th>Value</th></tr>
"""

    for key, value in results.items():

        html += f"<tr><td>{key}</td><td>{value}</td></tr>\n"

    html += "</table>"

    html += "<h2>Figures</h2>"

    for fig in figures:

        html += f"""

<h3>{Path(fig).stem.replace("_"," ").title()}</h3>

<img src="../{fig}">

"""

    html += """

<hr>

<p>

Generated automatically by Lambert W Copula

</p>

</body>

</html>

"""

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as f:

        f.write(html)