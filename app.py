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
    st.write("In the United States, there is a lack of laws about training mandated reporters. With these lack of regulations, this " \
    "map highlights the 22 U.S states and the District of Columbia that do not require specific training for mandated reporters, " \
    "forcing training resources to be up to the discretion of the job itself, or force the mandated reporter to follow additional information" \
    "to be sought out on their agency websites. The lack of regulation creates confusion for mandated reporters, forcing children to fall into" \
    "a system of neglect, trauma, and separation due to the miseducation of mandated reporters. Read on to continue learning about mandated reporter" \
    "laws in your state, and how to educate yourself if you're ever in a position to report.")


with st.expander('Warmlines'):
    st.header("Warmlines Across the United States")
    st.write("A warmline is a supportive, non-crisis helplines designed to assist families without automatically involving child protective services." \
    "Warmlines provide a direct hotline for mandated reporters to call, especially in cases where a child is showing signs of neglect rather than abuse," \
    "or connecting impoverished families with additional resources rather than forced separation. As a mandated reporter, here are warmlines you can contact" \
    "if you believe a family needs help, or need advice when creating a report:")
    

with st.expander('Community Pathways'):
    st.header("Community Pathways Across the United States")