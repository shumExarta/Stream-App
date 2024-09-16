import streamlit as st
import streamlit.components.v1 as components
import time
from functions import zeniva_values_for_insights
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
 
zeniva_youtube, zeniva_x, zeniva_tiktok, zeniva_linkedin, zeniva_instagram, zeniva_facebook = zeniva_values_for_insights()

zeniva_first_html_code = f"""
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
    top: 20px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}

.image-containerx img {{
    width: 40px; /* Adjust as needed */
    height: auto;
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
    </style>

        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>

    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <img src="https://s3-alpha-sig.figma.com/img/eade/289a/e18354455a369ad15c69d06cf3a4b8d9?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=WIBKSu6Km2Ruzy2rd1AES~qlUV14~IIUDn3Xf0hDzJmuIwJL~D5IJpEbxtON7d23YoKvR9p779yudRx17-rFfwb-D5E-sNl3bTsflBxzKGkZ51VDYRqP~vhDAUKjKEV4~iAY-fqOsNy7DyhzOhMkDxfZF6SxZGmh7DGrOqT8KlJ6i2mzH6IGSkn0G7LDUDpmeS0CBxpcwXYaeJw8ZXYsFiPm4ZzvC5z17axAsRIxs9DExbgSKMDI2Wo32WatugfErS5s4kJJktNsjDhrZ262aEWWGFnetUNuYzXnACstbuokoWV~WhYdeBHhlVmiIViODyXh6W4n7TnHG0qon-fhbA__" alt="logo" style="width:100px;">
            <div>
                <a href="#overview" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Overview</a>

                <a href="#zeniva" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline; text-decoration-color: none;">Zeniva</a>

                <a href="#odyessey" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Odyessey</a>

                <a href="#exarta" style="padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Exarta</a>

            </div>
        </div>
    </div>
    <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;'>Social Media</h2>
    <div class="main-container">
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/1498/18fb/0109e9eb56d423e70f5960980428bd58?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=SyHFjAnXlmYdYKWgvjqlg92uj8GHJDrg-dGbSfrmWFe-U3ZqoXKYBE37yAoeOFRH6OKsxSCi-Lz56srq-JJVMAxasuua05uVj3iAjLQdLjj42QbsS3BP~STGfGuChceh1gKUkwHz8-kJFcZ3fdBctjTv~x2KtCRj0p~e8Y6nyRsNTV4GyjCxjglPCZPTuoY2I7v95PvveiM5DoLLblfLL872rCNmvz~mf~zOEM~neP2vorcddB5MGLkKCvdJuAic3qR5zWkEzNdQd3dQ7A1ap-XxMgtbglne1oP2xaP~Tf5I0Q14CfgntY54P5lOHCKh0tDxBaDrynK18TzAJlXmug__" alt="logo">
        </div>
    <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_youtube['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_youtube['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_youtube['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-containerx">
            <img src="https://s3-alpha-sig.figma.com/img/768f/342d/9e4a770de98237a79973f9654303f292?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=E6d8o2dSlDUvxzppxhpSgUcLso~sJXw5gMyvpC~SKzZppzZU4ar1kJCLlB~EZJ3oPTeaBo1p8mvcX2GiSORibb3xvrA2pwolo~tjntVjN-mUfacBwIEEtrZzvTDQV9lCGwqLK~NIwIrfam5czU9mSUiC1Wv3QQxdEsOPv7nQIIKlowDXnY10W7xzjLgaR6JuL6sd1Si6iPlxkiI7zCSkXJvcdUbKGqK2Ku-9Qzgwm32heT1aW5Pd7PM0devl~zT3d07RHjCJlK06IsZ4NoZEy-pHe6FRhlotWp2nuXaWOu2iFOU3X5ecoHjSacT3pHVndm3T6AFS5fy9X7h75V0tHQ__" alt="logo">
        </div>
<div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_x['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_x['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_x['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/b47c/7f6f/fc9958aff216c7090428e6fa1fa03889?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=e3YAIVFgpSCWkpysbgSsHUCQsQRl22MlQfJcDgsot9KMKGp0Hx1-yBhSkkBMrO~m0ZrMAXHwiReE6lTJEai6-NB9o2aeKMZ1pSwsQUDb9m8oit99HXtNSwQiPA1hUGK4z-uyE-3hMf7B7JKiGllEIUdXPAwxWy5srGsMLQdtsbS4R48K2O-VCyEzAR5jrwlHw4zBnWY6TSmXSJotXn71OvyEBu6XkUguLolUmPojsWqvydSLKp28~vOBCFcULADpCgiJb1HjQ1H5VuURAqQvuTK5-YLdRVGwWkBcBMp0Ktsw68ZAiAj0bSaQPoyf~FyTewhZnY8BZE4V~eKnEAOCKg__" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_tiktok['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_tiktok['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_tiktok['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/0a8d/0e25/1524028dffda5c43327cb4b962333b48?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=Ll9~1wi~ajZRStSgseZUgbuwaPbOAAS5YFePWwHaLzxCuA~enY1KFCIkVqo87YqccyTM5X-Ya0jQYzwFQjqoefTr1yaSxa-eMtcpXXsqmW9yXObOszC-mcpuuZPN5NTlZyztwySHiB1OkW64cFuC~WGImderdzMPUWlGXBAaGjL986zquDeLc-ZjbKJZHcEnoG6QMIPvKenSnYCHDZ1JChVnW2Aus4I~-hEuEfvbWIwjKblvxwaCyeDXbecVDPpLoE4gCnWghdcOLBPBhA42xsDeocj-2TBvTDTjgDeiEe9GFBOSu4KL66e-f36ww4mGW-PIWaF-xX62jT4uHu51nA__" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_linkedin['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_linkedin['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_linkedin['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/232a/6d02/35389cdc480a936cb4b29721bb3a9670?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=hN8iUIM3AUxTXOHmt9VlXZ3uQxhl63pu1rEe8AzWjKArB7syWtDUbkz5yvkgZPytq3iRCUKqjUrzPp-MVCECluLH2KmgGrEK0W~galdt35yKHAme~gDsCb7ZeSJ0T20h4gfd4qpCCP82AWxBrK7ntSP80rVbSzQ3cwqknaXyMmtAC7Q5bYx9Dkor8ObVXax0NGQy26ASYHx8k9qfD3icj-mkQFrGzd4bsgF2g2~3d~dC2PK746Ez7TDcvwoBagvlEIky0YQzLYkOvrEmJmQaWHSZhPGebK-xumTxYYojLTrgaYaXA~ogiXiPuRKgSyLn3MnjY1mihWL0J3COVcH2kA__" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_instagram['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_instagram['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_instagram['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://i.ibb.co/8dLDtzM/image-11.png" alt="logo">
        </div>
        <div class="metric-container">
    <div class="metric-row">
        <p class="metric-left">Today's Follower Gain</p>
        <p class="metric-right">{int(zeniva_facebook['today_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Yesterday's Follower Gain</p>
        <p class="metric-right">{int(zeniva_facebook['yesterday_followers'].iloc[0])}</p>
    </div>
    <div class="metric-line"></div>

    <div class="metric-row">
        <p class="metric-left">Total Followers</p>
        <p class="metric-right">{int(zeniva_facebook['total_followers'].iloc[0])}</p>
    </div>
</div>
    </div>


</div>
"""


components.html(zeniva_first_html_code, height=1000)
time.sleep(10)
st.switch_page("pages/zeniva_second.py")