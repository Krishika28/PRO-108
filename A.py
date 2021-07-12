import pandas as p
import plotly_express as px
import plotly.figure_factory as ff

df = p.read_csv("data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()