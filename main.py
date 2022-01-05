import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

totals_df = daily_df[["Confirmed","Deaths","Recovered"]].sum().reset_index(name="count")

totals_df = totals_df.rename(columns={'index': "condition"})

countries_df = daily_df[["Country_Region","Confirmed","Deaths","Recovered"]]

countries_df = countries_df.groupby("Country_Region").sum().reset_index()

confirmed = daily_df.drop(["Province/State","Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name="total")

confirmed = confirmed.rename(columns={'index':"date"})
