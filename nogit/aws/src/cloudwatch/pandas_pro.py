import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
#print(np.random.rand(100, 5))
df = pd.DataFrame([[33256]], columns=["TotalUsers"])
#profile = ProfileReport(df, title="Welcome to IdP Reporting")
profile = df.profile_report(
    interactions ={
        "continuous":False,
    },
    correlations={
        "pearson": {"calculate": False},
        "spearman": {"calculate": False},
        "kendall": {"calculate": False},
        "phi_k": {"calculate": False},
        "cramers": {"calculate": False},
    },
    missing_diagrams={
        "heatmap": False,
        "dendrogram": False,
        "matrix":False,
        "bar":False,
    },
    title="IdP Reporting",
    sort="ascending",
    variables = {
        "descriptions":{
            "Explicaicon por dentro":"VAmos a ver"
        }
    },
    vars={
        "num": {
            "quantiles":[0.0,1.0],
            "skewness_threshold":0,
            "low_categorical_threshold": 0,
        },
        "cat": {
            "length": False,
            "characters": False,
            "words": False,
            "cardinality_threshold":0,
            "chi_squared_threshold":0.0,
            "n_obs": 0,
        },
        "bool": {
            "n_obs": 0
        }
    },
)

profile.config.variables.descriptions = {
    "TotalUsers": "Usuarios ingresados durante la semana",
}

profile.config.html.minify_html = True
profile.to_file("report.html")

#profile.to_file("your_report.html")