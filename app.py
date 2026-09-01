import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Mandated Reporting Solutions",  # the page title shown in the browser tab
    layout="wide",  # page layout : use the entire screen
)

st.title("Mandated Reporting Solutions")

with st.expander('About'):
    st.header("Miseducation of Mandated Reporters Across the United States")
    
    df = pd.DataFrame(
        {"state": ["AZ", "AR", "CO", "GA", "ID", "IN", "KS", "KY", "MI", "MS", "NE", "NH",
                   "NM", "NC", "ND", "OH", "OR", "RI", "SD", "TX", "VA", "WY"]}
    )

# Arizona, Arkansas, Colorado, Georgia, Idaho, Indiana, Kansas, Kentucky, Michigan, Mississippi, Nebraska, New Hampshire,
# New Mexico, North Carolina, North Dakota, Ohio, Oregon, Rhode Island, South Dakota, Texas, Virginia, and Wyoming

    # Create a US choropleth map
    fig = px.choropleth(
        df,
        locations="state",
        locationmode="USA-states",
        scope="usa",
        color_discrete_sequence=["tomato"],
    )

    # Render in Streamlit
    st.plotly_chart(fig)
    st.write("Testing")

with st.expander('Warmlines'):
    st.header("Warmlines Across the United States")
    

with st.expander('Community Pathways'):
    st.header("Community Pathways Across the United States")