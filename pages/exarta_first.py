import streamlit as st
import streamlit.components.v1 as components
import time
from functions import exarta_values_for_insights

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

st.markdown(
    """
    <style>
   
   header {visibility: hidden;}       
   footer {visibility: hidden;}         
   .stApp > header {display: none;}   

    
    
    /* Ensure all content aligns properly in the dark background */
    .stApp {
        background-color: #191B21;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)



exarta_youtube, exarta_x, exarta_facebook, exarta_linkedin, exarta_instagram = exarta_values_for_insights()
exarta_first_html_code = f"""
    <style>
    .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        color: white;
    }}
    .main-container {{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 20px;

}}

.main-card {{
    background-color: #272B34;
    height: 280px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
}}

.image-container {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-container img {{
    width: 100px; /* Adjust as needed */
    height: auto;
}}


.image-containerx {{
    position: absolute;
    top: 23px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containerx img {{
    width: 35px; /* Adjust as needed */
    height: 32px;
}}
    .card {{
        background-color: #343844;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        height: 170px;
    }}
    .paid-installs {{
        background-color: #A6B174;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-installs {{
        background-color: #F68C5B;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .today-paid-users {{
        background-color: #BC679C;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    .row {{
        display: flex;
        justify-content: space-between;
    }}
    .column {{
        flex: 1;
        margin: 0 10px;
    }}
    .number-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 48px;
        font-style: normal;
        font-weight: 800;
        line-height: normal;
    }}
    .card-text {{
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 26.172px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }}
    .graph-container {{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .metric-container {{
            margin-top: 100px;
        }}
        .metric-row {{
            display: flex;
            justify-content: space-between;

            padding: 10px 0;
        }}
        .metric-row p {{
            margin: 0;
        }}
        .metric-line {{
            border-bottom: 1px solid rgba(209, 209, 209, 0.1); /* Correct property for creating a line */
            margin: 10px 0;
        }}
        .metric-left {{
            color: #F0F0F0;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 300;
            line-height: normal;
            text-align: left;
        }}
        .metric-right {{
            color: white;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
            text-align: right;
        }}
                .progress-container {{
    width: 100%; /* Full width relative to the parent container */
    max-width: 1800px; /* Maximum width to ensure it doesn't exceed 1800px */
    height: 10px;
    background-color: #323743; /* Background color of the entire container */
    border-radius: 0px; /* No rounding for the container edges */
    overflow: hidden; /* Ensures that the progress bar stays within the container */
    margin: 0 auto; /* Center the progress container */
}}
 
.progress-bar {{
    width: 0; /* Initial width of the progress bar */
    height: 100%; /* Full height of the container */
    background: #495161; /* Progress bar color */
    border-radius: 5px;
    animation: grow 60s linear forwards; /* Animation: grow over 10 seconds */
}}
 
@keyframes grow {{
    from {{
        width: 0;
    }}
    to {{
        width: 100%; /* Grow to full width */
    }}
}}

 .image-containery {{
    position: absolute;
    top: 0px; /* Adjust as needed */
    left: 10px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containery img {{
    width: 100px; /* Adjust as needed */
    height: 80px;
}}

.image-containeri {{
    position: absolute;
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containeri img {{
    width: 105px; /* Adjust as needed */
    height: 37px;
}}

    </style>

        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>

    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
             <img style="padding-left:100px;" src="https://i.ibb.co/0jT4xCS/Logo-2-1.png" alt="logo" style="width:100px;">
            <div>
                <a href="#overview" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Overview</a>
 
                <a href="#zeniva" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none; text-decoration-color: none;">Zeniva</a>
 
                <a href="#odyessey" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Odyssey</a>
 
                <a href="#exarta" style="padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline;">Exarta</a>

            </div>
        </div>
    </div>
     <div class="progress-container">
    <div class="progress-bar"></div>
</div>
    <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;'>Social Media</h2>
    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://s3-alpha-sig.figma.com/img/1498/18fb/0109e9eb56d423e70f5960980428bd58?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=SyHFjAnXlmYdYKWgvjqlg92uj8GHJDrg-dGbSfrmWFe-U3ZqoXKYBE37yAoeOFRH6OKsxSCi-Lz56srq-JJVMAxasuua05uVj3iAjLQdLjj42QbsS3BP~STGfGuChceh1gKUkwHz8-kJFcZ3fdBctjTv~x2KtCRj0p~e8Y6nyRsNTV4GyjCxjglPCZPTuoY2I7v95PvveiM5DoLLblfLL872rCNmvz~mf~zOEM~neP2vorcddB5MGLkKCvdJuAic3qR5zWkEzNdQd3dQ7A1ap-XxMgtbglne1oP2xaP~Tf5I0Q14CfgntY54P5lOHCKh0tDxBaDrynK18TzAJlXmug__" alt="logo">
        </div>
    <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_youtube['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_youtube['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_youtube['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containerx">
            <img src="https://s3-alpha-sig.figma.com/img/768f/342d/9e4a770de98237a79973f9654303f292?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=E6d8o2dSlDUvxzppxhpSgUcLso~sJXw5gMyvpC~SKzZppzZU4ar1kJCLlB~EZJ3oPTeaBo1p8mvcX2GiSORibb3xvrA2pwolo~tjntVjN-mUfacBwIEEtrZzvTDQV9lCGwqLK~NIwIrfam5czU9mSUiC1Wv3QQxdEsOPv7nQIIKlowDXnY10W7xzjLgaR6JuL6sd1Si6iPlxkiI7zCSkXJvcdUbKGqK2Ku-9Qzgwm32heT1aW5Pd7PM0devl~zT3d07RHjCJlK06IsZ4NoZEy-pHe6FRhlotWp2nuXaWOu2iFOU3X5ecoHjSacT3pHVndm3T6AFS5fy9X7h75V0tHQ__" alt="logo">
        </div>
<div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_x['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_x['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_x['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://i.ibb.co/8dLDtzM/image-11.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_facebook['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_facebook['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_facebook['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/0a8d/0e25/1524028dffda5c43327cb4b962333b48?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=Ll9~1wi~ajZRStSgseZUgbuwaPbOAAS5YFePWwHaLzxCuA~enY1KFCIkVqo87YqccyTM5X-Ya0jQYzwFQjqoefTr1yaSxa-eMtcpXXsqmW9yXObOszC-mcpuuZPN5NTlZyztwySHiB1OkW64cFuC~WGImderdzMPUWlGXBAaGjL986zquDeLc-ZjbKJZHcEnoG6QMIPvKenSnYCHDZ1JChVnW2Aus4I~-hEuEfvbWIwjKblvxwaCyeDXbecVDPpLoE4gCnWghdcOLBPBhA42xsDeocj-2TBvTDTjgDeiEe9GFBOSu4KL66e-f36ww4mGW-PIWaF-xX62jT4uHu51nA__" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_linkedin['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_linkedin['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_linkedin['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containeri">
            <img src="https://i.ibb.co/XFh4Bvy/insta.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower </p>
        <p class="metric-right">{int(exarta_instagram['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower </p>
        <p class="metric-right">{int(exarta_instagram['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(exarta_instagram['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    
    </div>


</div>
"""
components.html(exarta_first_html_code, height=1000)
time.sleep(60)
st.switch_page("./main.py")