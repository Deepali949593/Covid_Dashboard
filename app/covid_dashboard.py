import streamlit as st
import pymongo
import pandas as pd
import plotly.express as px

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017"  # Change for Atlas if needed
client = pymongo.MongoClient(MONGO_URI)
db = client["covidDB"]
collection = db["covidData"]

st.title("🌍 COVID-19 Global Dashboard")

# Load data from MongoDB
data = list(collection.find().sort("fetchedAt", -1).limit(200))
df = pd.DataFrame(data)
df = df[["country", "cases", "deaths", "recovered", "population"]]

# Sidebar filter
country = st.sidebar.selectbox("Select Country", df["country"].unique())

selected = df[df["country"] == country].iloc[0]

st.metric("Total Cases", selected["cases"])
st.metric("Deaths", selected["deaths"])
st.metric("Recovered", selected["recovered"])
st.metric("Population", selected["population"])

# Show top 10 countries bar chart
top10 = df.sort_values("cases", ascending=False).head(10)
fig = px.bar(top10, x="cases", y="country", orientation="h", title="Top 10 Countries by Cases")
st.plotly_chart(fig, use_container_width=True)
