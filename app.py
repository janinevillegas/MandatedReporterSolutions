import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Mandated Reporting Solutions",  # the page title shown in the browser tab
    layout="wide",  # page layout : use the entire screen
)

st.title("Mandated Reporting Solutions")
st.image("https://simplelearning.com/images/uploads/announcing-the-launch-of-mandated-reporter-training-by-simple.jpg", use_container_width=True, caption="Image Credits: Simple Learning Systems")

st.header("The Miseducation of Mandated Reporters Across the United States")

df = pd.DataFrame(
    {"state": ["AZ", "AR", "CO", "GA", "ID", "IN", "KS", "KY", "MI", "MS", "NE", "NH",
                "NM", "NC", "ND", "OH", "OR", "RI", "SD", "TX", "VA", "WY"]}
)

# Create a US choropleth map
fig = px.choropleth(
    df,
    locations="state",
    locationmode="USA-states",
    scope="usa",
    color_discrete_sequence=["tomato"],
)

# Render in Streamlit
st.plotly_chart(fig, width="stretch")
st.write("In the United States, there is a lack of laws about training mandated reporters. With these lack of regulations, this " \
"map highlights the 22 U.S states and the District of Columbia that do not require specific training for mandated reporters, " \
"forcing training resources to be up to the discretion of the job itself, or force the mandated reporter to follow additional information" \
"to be sought out on their agency websites. The lack of regulation creates confusion for mandated reporters, forcing children to fall into" \
"a system of neglect, trauma, and separation due to the miseducation of mandated reporters. Read on to continue learning about mandated reporter" \
"laws in your state, and how to educate yourself if you're ever in a position to report.")

st.header("Mandated Reporting Solutions")
st.write("To better understand how to become a better mandated reporter, read below about my solutions to the miseducation of mandated reporting." \
"Millions of children across the United States are impacted by unnecessary reports, so check out the resources underneath to see new resources you can" \
"contact if you or anybody you know is at risk.")

st.markdown("""<style>
.button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #192269 !important;
    color: white !important;
    text-decoration: none !important;
    border-radius: 5px;
    font-weight: bold;
}

.button:hover {
    background-color: #192269 !important;
    color: white !important;
    text-decoration: none !important;
}
</style>
""", unsafe_allow_html=True)

with st.expander('Warmlines'):
    st.header("Warmlines Across the United States")
    st.write("A warmline is a supportive, non-crisis helplines designed to assist families without automatically involving child protective services." \
    "Warmlines provide a direct hotline for mandated reporters to call, especially in cases where a child is showing signs of neglect rather than abuse," \
    "or connecting impoverished families with additional resources rather than forced separation. As a mandated reporter, here are warmlines you can contact" \
    "if you believe a family needs help, or need advice when creating a report:")


    option = st.selectbox(
        "Warmlines By State",
        ("Select your state", "California", "Colorado", "Connecticut", "Idaho", "Minnesota", "New York", "Ohio", "Washington", "Washington DC")
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

        call_button_html = """
            <a class="button" href="tel:+18009262588"> Call 211 Here</a>
        """

        st.markdown(call_button_html, unsafe_allow_html=True)

        st.write("For more information, access their website here:")
        st.markdown("""<a class="button" href="https://healthandwelfare.idaho.gov/services-programs/211">211 Idaho Warmline</a>
        """, unsafe_allow_html=True)
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
    else:
        st.write("Can't find your state? Access this database to find resources near your Zip Code")
        st.markdown("""<a class="button" href="https://www.findhelp.org/">FindHelp</a> """, unsafe_allow_html=True)


    

with st.expander('Community Pathways'):
    st.header("Community Pathways Across the United States")
    st.write("A lack of trust in public systems may impede families’ willingness to engage in voluntary prevention services that could benefit their " \
    "children by promoting safety, stability and well-being. With mandated reporting following unclear regulations and a miseducation among its reporters," \
    "providing resources to both the reporter and family remains especially necessary. In three U.S states/territories, they follow a new system, a community" \
    "pathway, to follow a 'Family First' approach.")

    st.write("The Family First Prevention Services Act ('Family First'), enacted in February 2018, created a federal entitlement with the stated purpose of "
    "reducing entries into foster care by allowing states and Tribes to use federal Title IV-E funds for prevention services that support children to live "
    "safely with their families. The law provided an unprecedented opportunity to reorient child welfare and advance system transformation in regard to the "
    "types of services offered, which families receive services, and how and where they access them.")

    st.write("Read more about the three new approaches with a 'Family First' apprach.")

    option = st.selectbox(
        "Community Pathways By State",
        ("Select your state", "Connecticut", "Indiana", "Washington DC")
    )

    if option != "Select your state":
        st.write("You selected:", option)
    if option ==  "Connecticut":
        st.write("In 2023, Connecticut created a central place for families to call or " \
        "be referred when they need support. This prevention care management entity is " \
        "empowered to connect families to services without any direct contact with the child " \
        "protection agency. This model takes a public health approach in which any family can call "
        "and talk to an engagement specialist about their concerns and get connected to a resource "
        "or service that meets their individual needs.")

        st.write("Read more abou their community pathway approach here:")
        st.link_button("Connecticut Community Pathway", "https://portal.ct.gov/-/media/DCF/CTFamilyFirst/pdf/State-of-Connecticut-Family-First-Plan-January-2022_FINAL.pdf")
    elif option == "Indiana":
        st.write("In Indiana, the Department of Child Services turned to Healthy Families " \
        "America (HFA) as its initial community pathway provider and HFA-eligible families as the " \
        "population the state would serve. HFA has broad eligibility criteria with a focus on families " \
        "with risk of system involvement. The evidence-based model, which includes access to social, " \
        "economic, and concrete supports, has a service delivery infrastructure across the state and, " \
        "until recently, was funded largely through federal Temporary Assistance for Needy Families (TANF) " \
        "dollars. Indiana began claiming Title IV-E dollars through Family First for HFA in 2023. This " \
        "upstream investment has paid off. Indiana has administered the Healthy Families program statewide "
        "for over 30 years, and participation in the program has prevented child maltreatment in almost all "
        "(over 99%) of the families that receive 12 or more home visits, said Hannah Robinson, prevention " \
        "services manager at the Department of Child Services.")
    elif option == "Washington DC":
        st.write("Indiana began by turning to Healthy Families, an evidence-based home visiting program " \
        "already well-known and serving families across the state. With the bulk of service delivery infrastructure " \
        "already in place, moving to implementation mainly required the development of new tools and protocols related " \
        "to eligibility, safety monitoring, and reporting compliance. Indiana leverages Title IV-E funding for administrative " \
        "costs associated with staff administering the program, as well as for contracts to implement the model, monitor fidelity, " \
        "give quality assurance and technical assistance, and provide a database for collecting data.")
