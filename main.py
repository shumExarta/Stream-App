import streamlit as st
st.set_page_config(layout='wide')

# Custom CSS to style the cards
st.markdown("""
    <style>
    .main-card {
        background-color: #272B34;
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

# Create a 2x3 grid for the cards
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"""
        <div class="main-card">
            <div class="row">
                <h2>Zeniva</h2>
            </div>
            <div class="row">
                <div class="column">
                    <div class="paid-installs">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Paid Installs</p>
                    </div>
                </div>
                <div class="column">
                    <div class="today-installs">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Today's Installs</p>
                    </div>
                </div>
                <div class="column">
                    <div class="today-paid-users">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Today's Installs</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">4</h2>
                        <p class="card-text">Today's Paid Uninstalls</p>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">200</h2>
                        <p class="card-text">Today's Free Uninstalls</p>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">2</h2>
                        <p class="card-text">Total Uninstalls</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
with col2:
    st.markdown(
        """
        <div class="main-card">
            <div class="row">
                <h2>Odyessey3D</h2>
            </div>
            <div class="row">
                <div class="column"A>
                    <div class="paid-installs">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Paid Installs</p>
                    </div>
                </div>
                <div class="column">
                    <div class="today-installs">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Today's Installs</p>
                    </div>
                </div>
                <div class="column">
                    <div class="today-paid-users">
                        <h2 class="number-text">134</h2>
                        <p class="card-text">Today's Installs</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">4</h2>
                        <p class="card-text">Today's Paid Uninstalls</p>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">200</h2>
                        <p class="card-text">Today's Free Uninstalls</p>
                    </div>
                </div>
                <div class="column">
                    <div class="card">
                        <h2 class="number-text">2</h2>
                        <p class="card-text">Total Uninstalls</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )