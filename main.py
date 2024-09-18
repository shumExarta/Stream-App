import streamlit as st
import streamlit.components.v1 as components
import time
from functions import zeniva_overview, odyessey_overview
import pandas as pd
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
 
df = pd.read_csv("comparisons.csv") 
df = df.fillna(0)

today_paid_installs_for_zin, todays_free_installs_zin, total_installs_zin, today__paid_uninstalls_zin, today_free_uninstalls_zin, total_uninstalls_zin= zeniva_overview(df)
today_forge_installs_for_ody, todays_free_installs_for_ody, total_installs_for_ody, today__forge_uninstalls_for_ody, today_free_uninstalls_for_ody, total_uninstalls_for_ody = odyessey_overview(df) 

html_code = f"""
    <style>
    .header {{
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        color: white;
    }}
    .main-container {{
    display: grid;
    grid-template-columns: repeat(2,1fr);
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
    width: 100px; /* Adjust as needed */
    height: 29px;
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
 
 
.main-card {{
    background-color: #272B34;
    height: 400px;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
 
.firstrowcards {{
    display: flex;
    margin-top: 60px; /* Decrease this value to reduce space from the top */
    gap: 10px;
    margin-bottom: 0px; /* Reduce or remove space between rows */
}}
 
.secondrowcards {{
    display: flex;
    gap:10px;
    margin-top: 5px; /* Optional: add a small margin between the rows */
    margin-bottom: 10px;
}}
 
.card {{
    background-color: #444B57;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card1 {{
    background-color:#A6B174  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card2 {{
    background-color:#F68C5B  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
.card3 {{
    background-color:#BC679C  ;
    width: 32%;
    height: 150px;
    display: flex;
    flex-direction: column; /* Ensure items are aligned vertically */
    justify-content: center; /* Center vertically */
    align-items: flex-start; /* Align text to the left */
    border-radius: 5px;
    padding: 10px; /* Add some padding inside the card */
}}
 
 
.card-number {{
    font-size: 3em; /* Adjust this for a larger number */
    font-weight: 800;
    color: white; /* Adjust the color to your preference */
    margin-bottom: 5px; /* Add spacing between number and text */
}}
 
.card-text {{
 
font-family: Roboto;
font-size: 15px;
font-style: normal;
font-weight: 600;
line-height: normal;
margin-bottom: 22px;
}}
 
.progress-container {{
    width: 100%; /* Full width relative to the parent container */
    max-width: 1800px; /* Maximum width to ensure it doesn't exceed 1800px */
    height: 10px;
    background-color: #323743; /* Background color of the entire container */
    border-radius: 5px; /* No rounding for the container edges */
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
    </style>
 
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        </head>
 
    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
                       <img style="padding-left:100px;" src="https://i.ibb.co/0jT4xCS/Logo-2-1.png" alt="logo" style="width:100px;">
            <div>
                 <a href="#overview" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline; text-decoration-color: none;">Overview</a>
 
                <a href="#zeniva" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Zeniva</a>
 
                <a href="#odyessey" style="margin-right: 20px; padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Odyessey</a>
 
                <a href="#exarta" style="padding-right:50px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Exarta</a>
 
            </div>
        </div>
    </div>
      <div class="progress-container">
    <div class="progress-bar"></div>
</div>
    <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;'>Social Media</h2>
    <div class="main-container">
   
   
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/deec/0d17/7bdf715624ed952d97ee1983147bfc6e?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=pyO31F-qz-z0CLi5UvzoiaWq9M7tQDNoE-Q1sVaBs3S7NsqoAHIQNHR~6yVyZLHdNEvPDLK-3WzZonDQl9poH7plIafYAEkAxZusBnLN7VG7kuKWXn~4WjhHUWuAnaSfTAZw2Tkg06D0RAQIt6vXtKMTx5kXLIIT7OdFaEQEOh60wc678TSP7Stsmj~Wt1fnddUXv0quWbV3Y2XDddgFcp1epEf87u4fW61VS59ybIWvMM5~AD~EYAMA16iRaoK2Loty1HEOshc4wbcPXDK5JJvggglpFmxogxFtrnd0obgq5BH-~eG7CFGIT5vSDZcZ-659DrY0zotj-OdQ97Mkzw__" alt="logo">
        </div>
 
         <div class="firstrowcards">
         <div class="card1">
        <p class="card-number">{int(today_paid_installs_for_zin)}</p>
        <p class="card-text">Today's Paid Installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{todays_free_installs_zin}</p>
        <p class="card-text">Today's Free Installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{total_installs_zin}</p>
        <p class="card-text">Total Installs</p>
    </div>
    </div>
  <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(today__paid_uninstalls_zin)}</p>
        <p class="card-text">Today's Paid Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{today_free_uninstalls_zin}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{total_uninstalls_zin}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
   
    </div>
    <div class="main-card">
        <div class="image-containerx">
            <img src="https://s3-alpha-sig.figma.com/img/0b46/6838/becbd639884fea2ce7449a6c2aabe320?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=G9EWcixOfdO2nvhMdTQyHfbeF93K-hq6FQsT51C8WLQwSJ~wHs2gpbJ7E1xOqM4qV9HkhZapkOJRXWPfI-4xIpzX30xKx3lAyB486aAJpG9NJcm8fJri4h-T0SRGtG2-Xakyixb89N-o-nqQOrrdv01o0gWbDGA~Zr2ve9Z078hLKRY8N~5Zuzy86h2GrQN5a7Wj6N6UIYJdQwA85CadOiIjQ7V5FyKYfNKIYxAoYK~uBv74TJ7oytGOXipxykRPjMEqp2NMPRKSUauC4ZXeKdWNoaeZNFTFfQsZziia6--U8OSFsrcG2AkbTgaiQFRReOQCknFCqMsiNZAm8LeKkA__" alt="logo">
        </div>
 
 <div class="firstrowcards">
        <div class="card1">
        <p class="card-number">{int(today_forge_installs_for_ody)}</p>
        <p class="card-text">Today's Forge installs</p>
    </div>
    <div class="card2">
        <p class="card-number">{todays_free_installs_for_ody}</p>
        <p class="card-text">Today's Free installs</p>
    </div>
    <div class="card3">
        <p class="card-number">{total_installs_for_ody}</p>
        <p class="card-text">Total installs</p>
    </div>
    </div>
     <div class="secondrowcards">
    <div class="card">
        <p class="card-number">{int(today__forge_uninstalls_for_ody)}</p>
        <p class="card-text">Today's Forge Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{today_free_uninstalls_for_ody}</p>
        <p class="card-text">Today's Free Uninstalls</p>
    </div>
    <div class="card">
        <p class="card-number">{total_uninstalls_for_ody}</p>
        <p class="card-text">Total Uninstalls</p>
    </div>
</div>
</div>
   
   
   
</div>
"""
 
 

components.html(html_code, height=1000)
time.sleep(60)
st.switch_page("pages/zeniva_first.py")