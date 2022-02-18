import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("meta.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["mobile rating"])
fig.show()
