import streamlit as st
import streamlit.components.v1 as components
import time
from functions import plot_histograms_zeniva
 

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



odyssey_youtube_plot = plot_histograms_zeniva("odyssey", "youtube")
odyssey_meta_plot = plot_histograms_zeniva("odyssey", "meta")
odyssey_shopify_plot = plot_histograms_zeniva("odyssey", "shopify")
odyssey_ppc_plot = plot_histograms_zeniva("odyssey", "ppc")
 
 
ody_second_html_code = f"""
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
    height: 265px;
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

.image-containers {{
    position: absolute;
    top: 12px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containers img {{
    width: 100px; /* Adjust as needed */
    height: 45px;
}}

.image-containerp {{
    position: absolute;
    top: 22px; /* Adjust as needed */
    left: 20px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containerp img {{
    width: 100px; /* Adjust as needed */
    height: 25px;
}}

 
 .image-containery {{
    position: absolute;
    top: 3px; /* Adjust as needed */
    left: 10px; /* Adjust as needed */
    background-color: #272B34; /* Match the background color if necessary */
}}
 
.image-containery img {{
    width: 100px; /* Adjust as needed */
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
        padding-top:26px;
     
        width: 100%;
        height: 90%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
 
    .container {{
            display: flex;
            align-items: center; /* Align items vertically in the center */
            justify-content: space-between; /* Evenly space the heading and buttons */
            margin-top:15px;
            margin-bottom: 15px;
        }}
        .container h2 {{
            color: white;
            margin: 0;
            font-size: 24px;
        }}
        .buttons {{
            display: flex;
            gap: 20px; /* Gap between buttons */
        }}
        .buttons button {{
            padding: 10px 20px;
            font-size: 16px;
            background-color: #20232A;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
           
            text-align: center;
            font-family: Inter;
            font-size: 18px;
            font-style: normal;
            font-weight: 500;
            line-height: normal;
        }}
        .buttons button:hover {{
            background-color: #181A1F;
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
 
                <a href="#odyssey" style="margin-right: 20px; padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: underline;">Odyssey</a>
 
                <a href="#exarta" style="padding-right:100px; color: #F0F0F0; font-family: 'Roboto', sans-serif; font-size: 25px; font-style: normal; font-weight: 300; line-height: normal; text-decoration: none;">Exarta</a>
 
            </div>
        </div>
       
    </div>
         <div class="progress-container">
    <div class="progress-bar"></div>
</div>
     <div class="container">
        <h2 style='text-align:left; color:white;font-family: Roboto; font-size: 30px; font-style: normal;font-weight: 600; line-height: normal;' >Paid Campaigns</h2>
        <div class="buttons">
            <button>Today</button>
            <button>Week</button>
            <button>Month</button>
        </div>
    </div>
    <div class="main-container">
    <div class="main-card">
        <div class="image-containery">
            <img src="https://s3-alpha-sig.figma.com/img/1498/18fb/0109e9eb56d423e70f5960980428bd58?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=SyHFjAnXlmYdYKWgvjqlg92uj8GHJDrg-dGbSfrmWFe-U3ZqoXKYBE37yAoeOFRH6OKsxSCi-Lz56srq-JJVMAxasuua05uVj3iAjLQdLjj42QbsS3BP~STGfGuChceh1gKUkwHz8-kJFcZ3fdBctjTv~x2KtCRj0p~e8Y6nyRsNTV4GyjCxjglPCZPTuoY2I7v95PvveiM5DoLLblfLL872rCNmvz~mf~zOEM~neP2vorcddB5MGLkKCvdJuAic3qR5zWkEzNdQd3dQ7A1ap-XxMgtbglne1oP2xaP~Tf5I0Q14CfgntY54P5lOHCKh0tDxBaDrynK18TzAJlXmug__" alt="logo">
        </div>
       <div class="graph-container">
            {odyssey_youtube_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/3594/73a6/5b3aabc35e871898875a6b1ffb78876b?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=igT33~5IbJNL7qwH~S5cKggq-Cg86mUCc0gKbfTajQgohuO4rqoXRWUMQYZhX8V7xcBzfJyA7-pE8wfvwz3zCxLJygsHcHbbvmYNHwXZoa2RBnXU6LjTDyfSVDsTYxuIM4RcxW8Klb2Ox-FPstWqOH064kysLr08HWJPg9dCHeHX0oVEZynsSslpOolWurM7PTWnrbZDa6O83o3dtRxlZz~721RA6TI-j-R35NpGeBI4f92LCe9bpmUUhDa5rLGtA8eKjP~cBp1~wzY9lc1Bm8M2GKeQ6oI-ySJwLTLmSetW6APhhyijThrVWmyTGnXFb0b07TdtKqb4oJn~95zB7Q__" alt="logo">
        </div>
        <div class="graph-container">
            {odyssey_meta_plot}
        </div>
    </div>
     <div class="main-card">
        <div class="image-containers">
            <img src="https://s3-alpha-sig.figma.com/img/e6bd/3966/e9e44a17e0bf09233723ecd1e89cd914?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=GZyVlz5q1wWIZriBDzhSv4QNpXx1cJCt5CJyn4FdlEn4rhh8cBpHVnIz30fnJU7MQogfJC5K4C8MfAVmu2FdCHlildJeHmrTwGwZl5ddiJYK4vb7BSKFNeszaUr1yLJTlGao~iYzVZbGV311PRMbbWRgsYhLXynI7wYsXei~-TbVX2~Wv8V4oXd22JLRVw5beLjopNEeT7-SX9Y-FVZYZ8mbOSvYyDwPAtGAnZ9KicNZ8CLDn9zeCYDQoK5sLYZiI8jnKvcXUvWlt5XzAXK0fin-mt3YXDZFYTa5jyqcbrCG01pHROSbWbaznxt8kSQkZlQI38V6Lu7zvtvJ~gPb0g__" alt="logo">
        </div>
        <div class="graph-container">
            {odyssey_shopify_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-containerp">
            <img src="https://s3-alpha-sig.figma.com/img/1afc/9544/949af83cd742b7811af1bcdbd4733987?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=pkNEntW5QoLf2UaMO3kS6Asf2rsEOLDF81e0GORQQTQoabuaE1xd3OzpckmlBiw6SNUrxWugKqxOoDH97Ivm4Ru3i0Cx0EFvi8nI9pZ1H~HDYleInX~FgBNqtK3is~~1LZrhGWEcoBoG09pW0MX55Yp7O7~8kDTt6ZH692YhGvJ4-SAm2wOPdSjQ-rRLVlwaO0dNmgOaLyKN~Tq7d2tEaGcG3OyzB2SSK2JuQqtYid6SEXrC0ysf~go9WZ2oPnj8o5cQMdPrvlpsL~DaKl4-YXolY5AqSZq31oZ1gjgj2gLT6YLmLYLG82OBY47Z5sUzlvmKI9bGm4pyLUhlQjhkkg__" alt="logo">
        </div>
        <div class="graph-container">
            {odyssey_ppc_plot}
        </div>
    </div>
   
   
</div>
"""
components.html(ody_second_html_code, height=1000)
time.sleep(60)
st.switch_page("pages/exarta_first.py")