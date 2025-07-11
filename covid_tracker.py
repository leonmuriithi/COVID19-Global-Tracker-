import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("owid-covid-data.csv")

df["date"] = pd.to_datetime(df["date"])
df.fillna(0, inplace=True)

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

global_cases = df.groupby("date")["total_cases"].sum()
plt.plot(global_cases.index, global_cases.values)
plt.title("Global COVID-19 Total Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

latest_date = df["date"].max()
latest_snapshot = df[df["date"] == latest_date]
top_deaths = latest_snapshot.groupby("location")["total_deaths"].sum().sort_values(ascending=False).head(10)

sns.barplot(x=top_deaths.index, y=top_deaths.values, palette="Reds_r")
plt.title(f"Top 10 Countries by Total Deaths as of {latest_date.date()}")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.histplot(df["new_cases"], bins=50, kde=True, color="skyblue")
plt.title("Distribution of Daily New Cases Globally")
plt.xlabel("New Cases")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

scatter_data = latest_snapshot[["location", "total_cases", "total_vaccinations"]]
scatter_data = scatter_data[scatter_data["total_cases"] > 0]

sns.scatterplot(
    data=scatter_data,
    x="total_cases",
    y="total_vaccinations",
    hue="location",
    legend=False,
    s=100
)
plt.title("Total Cases vs Total Vaccinations by Country")
plt.xlabel("Total Cases")
plt.ylabel("Total Vaccinations")
plt.tight_layout()
plt.show()