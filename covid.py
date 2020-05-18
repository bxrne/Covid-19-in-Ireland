import plotly.express as px
import pandas as pd

d = pd.read_csv("covid-ireland-18-5.csv")
d.head()

f=px.scatter(d, x="Date", y="ConfirmedCovidCases")
f.show()
