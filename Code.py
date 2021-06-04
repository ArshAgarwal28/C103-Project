import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("Projects\C103\data.csv")

figure = px.scatter(df, x="date", y="cases",
                    color="country", title="Total Cases in countries")

figure.show()
