import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Honeywell GTM Dashboard",
    layout="wide"
)

# Logo
st.image(
    "https://1000logos.net/wp-content/uploads/2020/09/Honeywell-Logo.png",
    width=180
)

# Title
st.title("Honeywell India Smart Infrastructure GTM Dashboard")

st.markdown("""
Strategic expansion dashboard analyzing smart infrastructure opportunities
across Indian metro cities for Honeywell Building Automation.
""")

# Load dataset
df = pd.read_csv("data.csv")

# KPI cards
col1, col2, col3 = st.columns(3)

col1.metric("Top Opportunity City", "Bangalore")
col2.metric("Highest Growth Sector", "Data Centers")
col3.metric("Projected Market Opportunity", "$500M+")

st.divider()

# Market opportunity chart
st.subheader("Market Opportunity by City")

fig1 = px.bar(
    df,
    x="City",
    y="Market_Size_USD_M",
    color="Sector",
    title="Market Opportunity Across Indian Cities"
)

st.plotly_chart(fig1, use_container_width=True)

# Priority matrix
st.subheader("Sector Prioritization Matrix")

fig2 = px.scatter(
    df,
    x="Automation_Readiness",
    y="Priority_Score",
    size="Market_Size_USD_M",
    color="Sector",
    hover_name="City",
    title="Automation Readiness vs GTM Priority"
)

st.plotly_chart(fig2, use_container_width=True)

# GTM recommendation
st.subheader("AI GTM Recommendation")

best = df.sort_values(
    by="Priority_Score",
    ascending=False
).iloc[0]

st.success(
    f"""
    Recommended Expansion Focus:

    City: {best['City']}
    Sector: {best['Sector']}

    Reason:
    High automation readiness, strong market size,
    and accelerating infrastructure demand.
    """
)

# Top opportunities table
st.subheader("Top Expansion Opportunities")

top_opportunities = df.sort_values(
    by="Priority_Score",
    ascending=False
).head(5)

st.dataframe(top_opportunities)

# Insights
st.subheader("Key Strategic Insights")

st.markdown("""
### Key Findings

- Bangalore and Hyderabad show the strongest expansion potential due to rapid smart infrastructure growth.

- Commercial real estate and data centers demonstrate the highest automation readiness.

- ESG adoption and rising energy costs are accelerating demand for smart building solutions.

### Recommended GTM Channels

1. Enterprise Direct Sales  
2. Real Estate Partnerships  
3. System Integrator Network
""")