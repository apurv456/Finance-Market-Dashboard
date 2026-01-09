import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


df = pd.read_csv("pages\cleaned_finance.csv")


st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Global Finance Market Dashboard")


# sidebar filter
st.sidebar.header("Filters")

sector = st.sidebar.multiselect("Select Sector",options=df["Sector"].unique(),
                                default=df["Sector"].unique())

market_event = st.sidebar.multiselect("Select Market Event",options=df["Market Event"].unique(),
                                      default=df["Market Event"].unique())

index_range = st.sidebar.slider("Index Change Percent Range",float(df["Index Change Percent"].min()),
                                float(df["Index Change Percent"].max()),
                                (float(df["Index Change Percent"].min()),float(df["Index Change Percent"].max())))

# applying filters
filtered_df = df[(df["Sector"].isin(sector)) & (df["Market Event"].isin(market_event)) &
                 (df["Index Change Percent"] >= index_range[0]) & (df["Index Change Percent"] <= index_range[1])]


# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total News", len(filtered_df))
col2.metric("Avg Index Change %", round(filtered_df["Index Change Percent"].mean(), 2))
col3.metric("Total Trading Volume", round(filtered_df["Trading Volume"].sum(), 2))

st.divider()

st.dataframe(filtered_df)


# Index Change % by Market Index
st.header("Index Change % by Market Index")
fig = px.bar(filtered_df, x="Market Index", y="Index Change Percent", color="Market Index")
st.plotly_chart(fig)
st.info("""Insight: This chart compares performance across market indices.
- Highlights which index gained or lost the most.
- Easy to identify market leaders and laggards on a given day or filtered period.
- Useful for quick comparative analysis.""")


# Market Index Change Trend Over Time
st.header("Index Change Trend Over Time")
fig = px.line(filtered_df, x="Date", y="Index Change Percent", color="Market Index", markers=True)
st.plotly_chart(fig)
st.info("""Insight: Shows how each market index moves over time.
- Identifies trends, volatility, and market cycles.
- Helps spot sudden spikes or crashes linked to news or events.""")


# Trading Volume by Sector
st.header("Trading Volume by Sector")
fig = px.bar(filtered_df, x="Sector", y="Trading Volume")
st.plotly_chart(fig)
st.info("""Insight: Displays sector-wise trading activity.
- High volume → strong interest or major news impact.
- Low volume → stable or less investor focus.""")

# Volume vs Index Change
st.header("Volume vs Index Change")
fig = px.scatter(filtered_df, x="Trading Volume", y="Index Change Percent", 
                 color="Sentiment", size="Trading Volume", hover_name="Headline")
st.plotly_chart(fig)
st.info("""Insight: Analyzes the relationship between price movement and trading volume.
- High volume + high index change → strong market conviction
- High volume + low change → indecision or consolidation""")


# Market Sentiment Distribution
st.header("Market Sentiment Distribution")
fig = px.pie(filtered_df, names="Sentiment")
st.plotly_chart(fig)
st.info("""Insight: Shows overall market mood (Positive / Neutral / Negative).
- Dominant sentiment reflects investor confidence.
- Sudden increase in negative sentiment may signal risk.""")


# Trading Volume Distribution by Sector
st.header("Trading Volume Distribution by Sector")
fig = px.box(filtered_df, x="Sector", y="Trading Volume")
st.plotly_chart(fig)
st.info("""Insight: Shows spread, median, and outliers in sector trading volumes.
- Identifies highly volatile sectors.
- Outliers indicate unusual trading activity.""")


# Distribution of Index Change Percent
st.header("Distribution of Index Change Percent")
fig = px.histogram(filtered_df, x="Index Change Percent", nbins=10)
st.plotly_chart(fig)
st.info("""Insight: Shows how index changes are distributed.
- Identifies whether most changes are small or extreme.
- Reveals market volatility patterns.""")


# Market Events Impact Across Sectors
st.header("Market Events Impact Across Sectors")
fig = px.density_heatmap(filtered_df, x="Market Event", y="Sector")
st.plotly_chart(fig)
st.info("""Insight: Highlights how different market events affect sectors.
- Darker cells = stronger impact.
- Shows event sensitivity by sector.""")

# Impact Level by Company
st.header("Impact Level by Company")
fig = px.treemap(filtered_df, path=["Impact Level", "Related Company"], values="Trading Volume")
st.plotly_chart(fig)
st.info("""Insight: Shows which companies are most affected by events.
- Larger blocks → higher trading volume impact.
- Easily identifies key players driving market movement.""")


# News Source to Sentiment Flow
st.header("News Source to Sentiment Flow")
fig = px.sunburst(filtered_df, path=["Source", "Market Event", "Sentiment"])
st.plotly_chart(fig)
st.info("""Insight: Tracks how news sources influence market sentiment.
- Shows which sources generate positive or negative sentiment.
- Helps detect bias or influence patterns.""")


# Trading Volume Trend by Sector Over Time
st.header("Trading Volume Trend by Sector Over Time")
fig = px.area(filtered_df, x="Date", y="Trading Volume", color="Sector")
st.plotly_chart(fig)
st.info("""Insight: Shows how sector participation changes over time.
- Rising area → increasing investor interest.
- Declining area → fading momentum.""")


# Index Change Percent vs Trading Volume by Market Index
st.header("Index Change Percent vs Trading Volume by Market Index")
fig = px.scatter(filtered_df, x="Index Change Percent", y="Trading Volume", 
                 size="Trading Volume", color="Market Index")
st.plotly_chart(fig)
st.info("""Insight: Compares performance vs liquidity across indices.
- High change + high volume → strong market confidence
- Low volume → weak or unstable movement""")

 
st.markdown("""<hr><p style="text-align:center">Global Finance Market Analysis - Done by Apurv</p>""", unsafe_allow_html=True)
