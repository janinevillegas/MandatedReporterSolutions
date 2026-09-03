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


    option = st.selectbox(
        "Warmlines By State",
        ("Select your state", "Washington DC", "New York", "Idaho", "Connecticut", "Ohio", "Colorado", "Minnesota", "Washington", "California")
    )

    if option != "Select your state":
        st.write("You selected:", option)
    if option == "Washington DC":
        st.write("211 Warmline began as part of the city's Thriving Families, Safer Children initiative. This new warmline was officially" \
        "launched on February 11, 2026, aiming to create a unified social services network to support residents with centralized access to" \
        "resources and referrals, while shifting away from the traditional child welfare model.")

        st.write("For more information access their website here:")
        st.link_button("DC 211 Warmline", "https://211warmline.dc.gov/")
    elif option == "New York":
        st.write("New York City:")
        st.write("The Administration for Children's Services staffs a Support Line for families seeking asistance with issues such as food," \
        "housing, childcare, and mental health, connecting families to support outside of traditional child protective services. This wide range" \
        "of free services and resources give mandated reporters new hotlines to access rather than immediately default to aggressive reports.")

        st.write("For more information access their website here:")
        st.link_button("NYC Support Line", "https://www.nyc.gov/site/acs/for-families/home.page")

        st.write("New York:")
        st.write("HEARS (Help, Empower, Advocate, Reassure, and Support) Family Line is operated through the state's Office of Children and Family" \
        "Services, connecting callers all throughout the state of New York. Anybody has access to contacting this warmline, which aims to reduce the number" \
        "of families entering the CPS system. As a mandated reporter, you can access the HEARS line at (888)554-3277 Monday through Friday from 8:30am to 8:00pm.")

        st.write("For more information, access the HEARS website here:")
        st.link_button("HEARS Warmline", "https://ocfs.ny.gov/programs/cwcs/hears.php")
    elif option == "Idaho":
        st.write("211 Idaho Careline housed within the state Department of Health and Welfare is a statewide community information and referral service that" \
        "has been developing a special focus on suppporting kinship caregivers by training two staff members to be experts on kinship care. This lowcost alternative" \
        "provides mandated reporters with an outlet to connect others with local nonprofits, charities, and faith-based organizations who can support them. To be" \
        "connected with this community dial 211 or (800)926-2588 or text 898211 to be connected to a 211 community resource specialist Monday-Friday 8:00am-6:00pm MST.")

        st.write("For more information, access their website here:")
        st.link_button("211 Idaho Warmline", "https://healthandwelfare.idaho.gov/services-programs/211")



    st.write("Can't find your state? Access this database to find resources near your Zip Code")
    st.link_button("FindHelp", "https://www.findhelp.org/")

    

with st.expander('Community Pathways'):
    st.header("Community Pathways Across the United States")