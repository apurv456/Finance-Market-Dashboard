import streamlit as st

st.set_page_config(page_title="Global Finance Market Analysis", layout="wide")


st.markdown("<h1 style= 'color:white; text-align:center'>Global Finance Market Analysis</h1>",unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Global-Financial-Markets-Evolution.png", width=900)

st.markdown("<p style= 'text-align:center'>This dataset contains 3,024 records of financial market news events and their impact on market indices, trading activity, and sentiment.</p>", unsafe_allow_html=True)


st.subheader("Dataset Overview")
st.markdown("""<table><tr><th>Column</th><th>Description</th></tr>
            <tr><td><b>Date</b></td><td>Date when the market news was reported</td></tr>
            <tr><td><b>Headline</b></td><td>News headline describing the event</td></tr>
            <tr><td><b>Source</b></td><td>News source (e.g., Bloomberg, Reuters)</td></tr>
            <tr><td><b>Market Event</b></td><td>Type of event (Interest Rate Change, Earnings, Policy Update, etc.)</td></tr>
            <tr><td><b>Market Index</b></td><td>Affected market index (e.g., NIFTY, SENSEX, NASDAQ)</td></tr>
            <tr><td><b>Index Change Percent</b></td><td>Percentage change in the index due to the event</td></tr>
            <tr><td><b>Trading Volume</b></td><td>Trading volume recorded after the news</td></tr>
            <tr><td><b>Sentiment</b></td><td>Market sentiment derived from the news (Positive, Negative, Neutral)</td></tr>
            <tr><td><b>Sector</b></td><td>Industry sector impacted (IT, Banking, Retail, etc.)</td></tr>
            <tr><td><b>Impact Level</b></td><td>Severity of impact (Low, Medium, High)</td></tr>
            <tr><td><b>Related Company</b></td><td>Major company associated with the news</td></tr></table>""", unsafe_allow_html=True)


st.header("Key Objectives")
st.markdown("""- Analyze the impact of financial news events on major market indices by tracking percentage changes and trading volume.
- Evaluate market sentiment (Positive, Negative, Neutral) and understand how sentiment influences short-term market movements.
- Identify high-impact market events such as interest rate changes, earnings announcements, and policy updates that cause significant volatility.
- Perform sector-wise analysis to determine which industries react most strongly to different market events.
- Study trading volume behavior before and after news releases to assess investor activity and market confidence.
- Compare performance across market indices (e.g., NIFTY, SENSEX, NASDAQ) under various market conditions.
- Build interactive dashboards using Streamlit and Plotly to enable dynamic filtering and real-time data exploration.
- Support data-driven decision-making by visualizing trends, patterns, and anomalies in financial markets.""")


st.header("Dashboard Visualizations")
st.markdown("""- KPI Cards – Total News Count, Average Index Change Percentage, Total Trading Volume
- Bar Chart – Index Change Percentage by Market Index
- Line Chart – Market Index Change Trend Over Time
- Bar Chart – Trading Volume by Sector
- Scatter Plot – Trading Volume vs Index Change Percentage (colored by Sentiment)
- Pie Chart – Market Sentiment Distribution
- Box Plot – Trading Volume Distribution by Sector
- Histogram – Distribution of Index Change Percentage
- Heatmap – Market Events Impact Across Sectors
- Treemap – Impact Level by Related Company (based on Trading Volume)
- Sunburst Chart – News Source → Market Event → Sentiment Flow
- Area Chart – Trading Volume Trend by Sector Over Time
- Scatter Plot – Index Change Percentage vs Trading Volume by Market Index""")


st.markdown("""<hr><p style="text-align:center">Global Finance Market Analysis - Done by Apurv</p>""", unsafe_allow_html=True)
