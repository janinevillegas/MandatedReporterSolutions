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
    elif option == "Connecticut":
        st.write("The Community Pathways warmline provides resource and referral support to families with children who are impacted by mental health and substance" \
        "use disorder concerns. Knowing who to call when a youth is struggling with mental health or substance use issues can be frustrating and confusing. If you " \
        "know of a youth under the age of 18 who is having troubles, call us and we will connect you to the services and community based supports that best meet the " \
        "family’s needs. We put families in the driver’s seat to create a plan that feels supported, sustainable, and effective. By calling (877)381-4193, then dialing" \
        "option 1 during regular business hours, you can contact a family peer specialist before ever entering another family into a broken system.")

        st.write("For more information access their website here:")
        st.link_button("Connecticut Warmline", "https://www.carelonbh.com/ctcfd/en/home/programs-supports/community-pathways")
    elif option == "Ohio":
        st.write("In 12 Ohio counties, callers to 211 or a crisis hotline may be referred to the Family Success Network, providing family coaches to assist with connections" \
        "to community services. This warmline is a voluntary program designed to strengthen and support businesses on their unique needs, rather than forcing a mandated reporter" \
        "to send an unsubstantiated report to a broken system.")

        st.write("For more information, access their website here:")
        st.link_button("Family Success Network", "https://octf.ohio.gov/what-we-do/family-success-network/family-success-network")
    elif option == "Colorado":
        st.write("A brand new three-county pilot has been implemented to provided a recorded message to hotline callers, describing child maltreatment and " \
        "directing callers to 211 to help families access services if the caller's concerns do not meet the criteria for maltreatment. By providing this recorded" \
        "message, it helps mandated reporters understand what is considered substantial to report, avoiding a flooded system for child protective services. This" \
        "warmline is designed to avoid any extra family stress, educating the mandated reporter of what is considered abuse or neglect.")

        st.write("For more information, access their website here:")
        st.link_button("Colorado Warmline", "https://foster-america.org/innovative-approach-to-support-families-launches-in-colorado/")
    elif option == "Minnesota":
        st.write("CPS helps callers determine if a suspected maltreatment report is warranted. However, mandated reporters have an option to" \
        "transfer to a consultation line, providing information about community services for families. Hennepin County, MN provides this opportunity" \
        "for mandated reporters to make a report, without the intervention of child protection staff. To make a child protection report, call (612)348-3552")

        st.write("For more information about Hennepin County's warmline, access their website here:")
        st.link_button("Hennepin County Warmline", "https://www.hennepincounty.gov/services/assistance/children-families/child-protection?from=childprotection")
    elif option == "Washington":
        st.write("The Parent Trust Family Helpline is a place for parents in the state of Washington who need someone to listen" \
        "to them. This allows for mandated reporters to connect families who need extra resources, rather than adding to an unsubstaniated" \
        "report to child protective services. If you need to connect directly to a Parent Coach, or know someone who does, contact them at" \
        "(800)932-4673 Monday through Friday from 9am to 5pm, or email them at familyhelpline@parenttrust.org.")

        st.write("For more information about Washington's Parent Trust program, you can access their website at:")
        st.link_button("Parent Trust", "https://www.parenttrust.org/for-families/call-fhl/")
    elif option == "California":
        st.write("In San Francisco, there is a warmline called Safe & Sound TALK Line, which pairs volunteers with" \
        "parents for peer support, serving as a front door for service referrals, including intensive case management." \
        "Rather than reporting directly, mandated reporters can connect parents to these volunteers to provide extra suppport" \
        "during troubling family periods. You or someone you know can access this helpline 9am to 10pm Monday through Friday" \
        "and Weekends from 9am to 6pm at (415)441-KIDS (5437)")

        st.write("For more information about San Francisco's warmline, you can access their website here:")
        st.link_button("Safe & Sound", "https://www.safeandsound.org/for-parents/get-help-now/")

    st.write("Can't find your state? Access this database to find resources near your Zip Code")
    st.link_button("FindHelp", "https://www.findhelp.org/")


    

with st.expander('Community Pathways'):
    st.header("Community Pathways Across the United States")