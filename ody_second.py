import streamlit as st
import streamlit.components.v1 as components
from functions import plot_histograms_zeniva

st.set_page_config(layout="wide")

odyessey_youtube_plot = plot_histograms_zeniva("odyessey", "youtube")
odyessey_meta_plot = plot_histograms_zeniva("odyessey", "meta")
odyessey_shopify_plot = plot_histograms_zeniva("odyessey", "shopify")
odyessey_ppc_plot = plot_histograms_zeniva("odyessey", "ppc")


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
    height: 300px;
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
    </style>

    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <img src="https://s3-alpha-sig.figma.com/img/eade/289a/e18354455a369ad15c69d06cf3a4b8d9?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=WIBKSu6Km2Ruzy2rd1AES~qlUV14~IIUDn3Xf0hDzJmuIwJL~D5IJpEbxtON7d23YoKvR9p779yudRx17-rFfwb-D5E-sNl3bTsflBxzKGkZ51VDYRqP~vhDAUKjKEV4~iAY-fqOsNy7DyhzOhMkDxfZF6SxZGmh7DGrOqT8KlJ6i2mzH6IGSkn0G7LDUDpmeS0CBxpcwXYaeJw8ZXYsFiPm4ZzvC5z17axAsRIxs9DExbgSKMDI2Wo32WatugfErS5s4kJJktNsjDhrZ262aEWWGFnetUNuYzXnACstbuokoWV~WhYdeBHhlVmiIViODyXh6W4n7TnHG0qon-fhbA__" alt="logo" style="width:100px;">
            <div>
                <a href="#overview" style="margin-right: 20px; color: white; text-decoration: none;">Overview</a>
                <a href="#zeniva" style="margin-right: 20px; color: white; text-decoration: none;">Zeniva</a>
                <a href="#odyessey" style="margin-right: 20px; color: white; text-decoration: none;">Odyessey</a>
                <a href="#exarta" style="color: white; text-decoration: none;">Exarta</a>
            </div>
        </div>
    </div>
    <h2 style='text-align: center;'>Social Media Stats</h2>
    <div class="main-container">
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/1498/18fb/0109e9eb56d423e70f5960980428bd58?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=SyHFjAnXlmYdYKWgvjqlg92uj8GHJDrg-dGbSfrmWFe-U3ZqoXKYBE37yAoeOFRH6OKsxSCi-Lz56srq-JJVMAxasuua05uVj3iAjLQdLjj42QbsS3BP~STGfGuChceh1gKUkwHz8-kJFcZ3fdBctjTv~x2KtCRj0p~e8Y6nyRsNTV4GyjCxjglPCZPTuoY2I7v95PvveiM5DoLLblfLL872rCNmvz~mf~zOEM~neP2vorcddB5MGLkKCvdJuAic3qR5zWkEzNdQd3dQ7A1ap-XxMgtbglne1oP2xaP~Tf5I0Q14CfgntY54P5lOHCKh0tDxBaDrynK18TzAJlXmug__" alt="logo">
        </div>
       <div class="graph-container">
            {odyessey_youtube_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/3594/73a6/5b3aabc35e871898875a6b1ffb78876b?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=igT33~5IbJNL7qwH~S5cKggq-Cg86mUCc0gKbfTajQgohuO4rqoXRWUMQYZhX8V7xcBzfJyA7-pE8wfvwz3zCxLJygsHcHbbvmYNHwXZoa2RBnXU6LjTDyfSVDsTYxuIM4RcxW8Klb2Ox-FPstWqOH064kysLr08HWJPg9dCHeHX0oVEZynsSslpOolWurM7PTWnrbZDa6O83o3dtRxlZz~721RA6TI-j-R35NpGeBI4f92LCe9bpmUUhDa5rLGtA8eKjP~cBp1~wzY9lc1Bm8M2GKeQ6oI-ySJwLTLmSetW6APhhyijThrVWmyTGnXFb0b07TdtKqb4oJn~95zB7Q__" alt="logo">
        </div>
        <div class="graph-container">
            {odyessey_meta_plot}
        </div>
    </div>
     <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/e6bd/3966/e9e44a17e0bf09233723ecd1e89cd914?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=GZyVlz5q1wWIZriBDzhSv4QNpXx1cJCt5CJyn4FdlEn4rhh8cBpHVnIz30fnJU7MQogfJC5K4C8MfAVmu2FdCHlildJeHmrTwGwZl5ddiJYK4vb7BSKFNeszaUr1yLJTlGao~iYzVZbGV311PRMbbWRgsYhLXynI7wYsXei~-TbVX2~Wv8V4oXd22JLRVw5beLjopNEeT7-SX9Y-FVZYZ8mbOSvYyDwPAtGAnZ9KicNZ8CLDn9zeCYDQoK5sLYZiI8jnKvcXUvWlt5XzAXK0fin-mt3YXDZFYTa5jyqcbrCG01pHROSbWbaznxt8kSQkZlQI38V6Lu7zvtvJ~gPb0g__" alt="logo">
        </div>
        <div class="graph-container">
            {odyessey_shopify_plot}
        </div>
    </div>
    <div class="main-card">
        <div class="image-container">
            <img src="https://s3-alpha-sig.figma.com/img/1afc/9544/949af83cd742b7811af1bcdbd4733987?Expires=1727654400&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=pkNEntW5QoLf2UaMO3kS6Asf2rsEOLDF81e0GORQQTQoabuaE1xd3OzpckmlBiw6SNUrxWugKqxOoDH97Ivm4Ru3i0Cx0EFvi8nI9pZ1H~HDYleInX~FgBNqtK3is~~1LZrhGWEcoBoG09pW0MX55Yp7O7~8kDTt6ZH692YhGvJ4-SAm2wOPdSjQ-rRLVlwaO0dNmgOaLyKN~Tq7d2tEaGcG3OyzB2SSK2JuQqtYid6SEXrC0ysf~go9WZ2oPnj8o5cQMdPrvlpsL~DaKl4-YXolY5AqSZq31oZ1gjgj2gLT6YLmLYLG82OBY47Z5sUzlvmKI9bGm4pyLUhlQjhkkg__" alt="logo">
        </div>
        <div class="graph-container">
            {odyessey_ppc_plot}
        </div>
    </div>
    
    
</div>
"""


# Embed the custom HTML with st.components.v1.html
components.html(html_code, height=1000)
