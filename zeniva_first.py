import streamlit as st
from functions import zeniva_values_for_insights
st.set_page_config(layout='wide')

zeniva_linkedin_followers = zeniva_values_for_insights()


# Custom CSS to style the cards
st.markdown("""
    <style>
    .main-card {
        background-color: #272B34;
        height: 300px;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        color: white;
    }
    .card {
        background-color: #343844;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        height: 170px;
    }
    .paid-installs {
        background-color: #A6B174;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .today-installs {
        background-color: #F68C5B;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .today-paid-users {
        background-color: #BC679C;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .row {
        display: flex;
        justify-content: space-between;
    }
    .column {
        flex: 1;
        margin: 0 10px;
    }
    .number-text {
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 48px;
        font-style: normal;
        font-weight: 800;
        line-height: normal;
    }
    .card-text {
        color: #F0F0F0;
        font-family: Roboto;
        font-size: 26.172px;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }
    .header {
        background-color: #20232A;
        padding: 20px;
        text-align: center;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Header with logo and clickable text elements
st.markdown("""
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
""", unsafe_allow_html=True)

# FIRST SET OF METRICS
st.header("Social Media")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f"""
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/1498/18fb/0109e9eb56d423e70f5960980428bd58?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=SyHFjAnXlmYdYKWgvjqlg92uj8GHJDrg-dGbSfrmWFe-U3ZqoXKYBE37yAoeOFRH6OKsxSCi-Lz56srq-JJVMAxasuua05uVj3iAjLQdLjj42QbsS3BP~STGfGuChceh1gKUkwHz8-kJFcZ3fdBctjTv~x2KtCRj0p~e8Y6nyRsNTV4GyjCxjglPCZPTuoY2I7v95PvveiM5DoLLblfLL872rCNmvz~mf~zOEM~neP2vorcddB5MGLkKCvdJuAic3qR5zWkEzNdQd3dQ7A1ap-XxMgtbglne1oP2xaP~Tf5I0Q14CfgntY54P5lOHCKh0tDxBaDrynK18TzAJlXmug__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>35</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>34</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
with col2:
    st.markdown(
        """
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/768f/342d/9e4a770de98237a79973f9654303f292?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=FhgU0xoY9xZro1SDHymYb4oxhnVl6ROxTLOuOS2hIAzPO6iT-tCE33wejsaW7nNV0yvcvv2ueGlyy8DVUSDXItj3vX90In6pN3AciNFP3T-CNvg-~4K7T0GBDT9KVAshn9P067X30flWmoFyHu58C5N~vC8P5jrjaSd95~SnkUlKx5wObIEYt5qWKyvJ49xFEkYF2IkNmvvdp8fzPCiFj4qhnc~bVvZ8vIShjzdstoQiVccGuLSR9HVbl6WSR6lk3Njepy5g45e4~mrPzp50uUO3oP0OIT9tEZgzkHEqwluKwhaTY8qPvPh1Op7rlQUA0VI2y42REZDOw5Rw0jhQNg__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>34</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
with col3:
    st.markdown(
        """
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/b47c/7f6f/fc9958aff216c7090428e6fa1fa03889?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=D-tG02lIx3PeUh7xYTjYgy9iDSNUVqrz4jCEJzVWFRoq0-sAJ6VZFIyVFAO2yn6LkdB~BDxTrwh1khDKt5nwXzbvVBXZmj4zGlyXW-Wr-PbNNFe3y5fP6gEifmN~v38-QZwmaggPSS3VgDjhK31p5aAS6hDMhKqugV-54W3oTBylGtRlNNWfIgLhdKeZ7YFEdY7YiCxDR7mY6Q09BcRh6rlH8I--ypi1n5Wf~FvMIik01KqmoW--qvdPAWaQ02Yl~jnKv5gCZM1c5YdOY5M0GJ2n77Hl6P7bWOg92t7xzm6c9kG6nOovX4unPdPG2T1-05IrDmJ37HmxT0COXlR2uw__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>34</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

# SECOND SET OF METRICS    
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(
        f"""
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/0a8d/0e25/1524028dffda5c43327cb4b962333b48?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=ku4i7TZmrk8Ku1D-gBBoMWHIwrwK9To~PB2-kg20vWSsCxYeUMFxggPPigi6tot1Z9VWYusvKTREG8jSrbYhdXs1M9lcUvlqyTIVPnEXP3bqEPVPLAAfqUB3p4GNtwdzxXZGwh0vKfK6rfrEZcDE2JnZqL9v-yJRBV9W0XSM4ZwjNvHAniHjvIFReEDrzVc0Xqgym4P5CxI55OBcNz68CZIbsPbPbKuac8oBdtOlxRJnQ7BFXXDMob8ZT~ZYF86X45Yu6N2RsB1s1cmEDQ4BYbyaLXYFjD39RKjEKdBnW8D30o6wnqY50MB9b4xm1Auy9jsYqwxD8LqWVeaOjOYn1w__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>{int(zeniva_linkedin_followers['today_followers'])}</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>{int(zeniva_linkedin_followers['yesterday_followers'])}</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>{int(zeniva_linkedin_followers['total_followers'])}</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
with col5:
    st.markdown(
        """
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/232a/6d02/35389cdc480a936cb4b29721bb3a9670?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=oK0XcCmpwGIRCY4NkO-cdFF-XE8aVxgIUZvbdoSDqLXFkTVmJg2Gjg1DNSffP~qTkcdME8z3IUr~QsBzWkSjXzI6SUI-fwZqM2XMhPFRw3-Z-UeCuE~6fiLFaXTiSOicVKOY1qi490fqiQtlsYM542vF3EEheuZ-2yEcmqYsZh5y6qqUS8s5n0H6bCPLNrOuSPwyCncfU6cSTmah-mA20BNtEUJvAWREoMAeV--9hxxSmaePeEPAgKOd~HcUs-pDVDHYE2DztmsYpKMMIdP4--2gGO7tIT6QN4x6OVtdK09FInrkNQ-u66O18reiJtuOTpmGz-wvhfgc9Pj0cIECgw__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>34</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
with col6:
    st.markdown(
        """
        <div class="main-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <img src="https://s3-alpha-sig.figma.com/img/8dc1/10ac/b5207b2f13bddf9c389553f59ecc26fc?Expires=1727049600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=A818FDLlVUQDYe9bKPfPdfqLkT7bl8B2Gh52lMli~rYMyErdDX3qSLI0Iob-6sj5PVkXbwti6f7K2aMm4x8RnF-u-RCyHLP2ho6YGXVHuscnI~jZZJs6aA07OZBtEH41suzjWfqUwfkm4WkCQYErmzjgfRp45LYq-JKPDTsMYFl87~YTwBdKyoTPzpQ0emjFEyqe-lws91l6sjgc3gbqQWRGW4TyMAowGzv9rkNfqiAHldzy1Eye0BenJKve16QNIDb3k~AUqXNqFsebh0B9nE05AdqHZ5x~OVgklnSC8AvF6CRAtnO9ATGRcW8K96BPyOxAVWtD7ROU4p7M9erBvw__" alt="logo" style="width:100px;">
            </div>
            <div class="row">
                <p>Today's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Yesterday's Follower Gain</p>
                <p>34</p>
            </div>
            <div class="row">
                <p>Total Followers</p>
                <p>34</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )