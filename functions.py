import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Manually format day and month without leading zeros
today_date = f"{today.day}/{today.month}/{today.strftime('%y')}"

# Append .xlsx to the formatted date
filename = today_date.replace('/', '-') + '.xlsx'

combined_Data = today_date.replace('/', '-') + '-Graphs_Data.csv'

file_path = filename
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet0')
df_sheet2 = pd.read_excel(file_path, sheet_name='Sheet1')
df_sheet3 = pd.read_excel(file_path, sheet_name='Sheet2')
live_data = pd.concat([df_sheet1, df_sheet2, df_sheet3], ignore_index=True)



def histo_youtube(dataframe):
    df_youtube = dataframe[dataframe["platform"] == "youtube"]
    youtube_melted = df_youtube.melt(
        id_vars=["date"],
        value_vars=["views", "clicks", "daily_spend"],
        var_name="metric",
        value_name="value",
    )

    df_meta = dataframe[dataframe["platform"] == "meta"]
    meta_melted = df_meta.melt(
        id_vars=["date"],
        value_vars=["views", "clicks", "daily_spend"],
        var_name="metric",
        value_name="value",
    )

    return youtube_melted, meta_melted


def filtering_data(dataframe):
    # FOR EXARTA
    filter_product_exarta = dataframe[dataframe["product"] == "exarta"]

    # FOR EXARTA YOUTUBE
    filter_youtube_exarta = filter_product_exarta[
        filter_product_exarta["platform"] == "youtube"
    ]
    youtube_melted = filter_youtube_exarta.melt(
        id_vars=["date"],
        value_vars=["views", "clicks", "daily_spend"],
        var_name="metric",
        value_name="value",
    )
    # FOR EXARTA META
    filter_meta_exarta = filter_product_exarta[
        filter_product_exarta["platform"] == "meta"
    ]
    meta_melted = filter_meta_exarta.melt(
        id_vars=["date"],
        value_vars=["views", "clicks", "daily_spend"],
        var_name="metric",
        value_name="value",
    )
    # FOR EXARTA PPC
    filter_ppc_exarta = filter_product_exarta[
        filter_product_exarta["platform"] == "ppc"
    ]
    ppc_melted = filter_ppc_exarta.melt(
        id_vars=["date"],
        value_vars=["views", "clicks", "daily_spend"],
        var_name="metric",
        value_name="value",
    )

    return youtube_melted, meta_melted, ppc_melted


def zeniva_values_for_insights():
    data = live_data.fillna(0)
    zeniva_data = data[data["product"] == "zeniva"]
    zeniva_youtube = zeniva_data[zeniva_data["platform"] == "youtube"]
    zeniva_x = zeniva_data[zeniva_data["platform"] == "x"]
    zeniva_tiktok = zeniva_data[zeniva_data["platform"] == "tiktok"]
    zeniva_linkedin = zeniva_data[zeniva_data["platform"] == "linkedin"]
    zeniva_instagram = zeniva_data[zeniva_data["platform"] == "instagram"]
    zeniva_facebook = zeniva_data[zeniva_data["platform"] == "facebook"]
    return (
        zeniva_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_x[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_linkedin[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        zeniva_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )


def odyssey_values_for_insights():
    data = live_data.fillna(0)
    odyssey_data = data[data["product"] == "odyssey"]
    odyssey_youtube = odyssey_data[odyssey_data["platform"] == "youtube"]
    odyssey_x = odyssey_data[odyssey_data["platform"] == "x"]
    odyssey_tiktok = odyssey_data[odyssey_data["platform"] == "tiktok"]
    odyssey_instagram = odyssey_data[odyssey_data["platform"] == "instagram"]
    odyssey_facebook = odyssey_data[odyssey_data["platform"] == "facebook"]
    return (
        odyssey_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_x[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )


def exarta_values_for_insights():
    data = live_data.fillna(0)
    exarta_data = data[data["product"] == "exarta"]
    exarta_youtube = exarta_data[exarta_data["platform"] == "youtube"]
    exarta_x = exarta_data[exarta_data["platform"] == "x"]
    exarta_facebook = exarta_data[exarta_data["platform"] == "facebook"]
    exarta_linkedin = exarta_data[exarta_data["platform"] == "linkedin"]
    exarta_instagram = exarta_data[exarta_data["platform"] == "instagram"]
    return (
        exarta_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_x[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_facebook[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_linkedin[["total_followers", "today_followers", "yesterday_followers"]],
        exarta_instagram[["total_followers", "today_followers", "yesterday_followers"]],
    )






def plot_histograms_zeniva(product_name, platform_name):
    # Load and preprocess the data
    df = pd.read_csv(combined_Data)
    df = df.fillna(0)
    df = df[df['product'] == product_name]

    platform_metrics = {
        'youtube': ['clicks', 'views', 'daily_spend'],
        'meta': ['clicks', 'reach', 'daily_spend'],
        'shopify': ['clicks', 'daily_spend', 'dummy_metric'],  # Add dummy metric for Shopify
        'ppc': ['clicks', 'daily_spend', 'impressions'],
    }

    if platform_name in platform_metrics:
        selected_metrics = platform_metrics[platform_name]
    else:
        st.error(f"Platform {platform_name} not recognised.")
        return

    df_platform = df[df['platform'] == platform_name]

    # Convert 'date' column to datetime format for easier comparison
    df_platform['date'] = pd.to_datetime(df_platform['date'], format='%m/%d/%Y')

    # Get the latest date available for the selected platform
    if df_platform.empty:
        st.error(f"No data available for platform {platform_name}.")
        return

    latest_date = df_platform['date'].max()

    # Get the last 3 available dates based on the latest date
    dates = [latest_date - timedelta(days=i) for i in range(3)]
    
    # Ensure formatted dates match the datetime format in the dataframe
    formatted_dates = [date.strftime("%m-%d-%y") for date in dates]

    # Filter the dataframe to include only the last 3 available dates
    df_filtered = df_platform[df_platform['date'].isin(dates)]

    # Create placeholders for missing dates if less than 3 are available
    available_dates = df_filtered['date'].dt.strftime('%m-%d-%y').unique().tolist()
    missing_dates = [date for date in formatted_dates if date not in available_dates]

    # If no data exists for the last 3 days, fall back to available dates
    if df_filtered.empty:
        st.error("No data available for the last 3 days.")
        return

    # Add dummy metric for Shopify to ensure consistent bar width
    if 'dummy_metric' in selected_metrics:
        df_filtered['dummy_metric'] = 0

    # Reshape the dataframe for plotting
    df_grouped = df_filtered[['date'] + selected_metrics].melt(id_vars='date', var_name='Metric', value_name='Value')

    # Define color mapping for metrics
    color_discrete_map = {
        'clicks': '#BC679C',
        'views': '#F68C5B',
        'daily_spend': '#A6B174',
        'reach': '#F68C5B',
        'impressions': '#F68C5B',
        'dummy_metric': '#FFFFFF'  # Invisible color for the dummy metric
    }

    label_map = {
            'clicks': 'Clicks',
            'views': 'Views',
            'daily_spend': 'Daily Spend',
            'reach': 'Reach',
            'impressions': 'Impressions',
            'dummy_metric': ''  # No label for the dummy metric
        }

    # Plot histogram
    fig = px.histogram(
        df_grouped, 
        x='date', 
        y='Value', 
        color='Metric', 
        barmode='group', 
        height=300,
        width=800,
        color_discrete_map=color_discrete_map,
    )

    fig.for_each_trace(lambda trace: trace.update(name=label_map.get(trace.name, trace.name)))

    # Extract unique dates for the x-axis and format them
    unique_dates = df_grouped['date'].dt.to_period('D').astype('str').unique()
    formatted_dates = [pd.to_datetime(date).strftime('%d %B') for date in unique_dates]

    # Update the layout to format x-axis labels
    fig.update_layout(
        xaxis=dict(
            tickvals=pd.to_datetime(unique_dates).to_pydatetime(),  # Set tick values to unique dates
            ticktext=formatted_dates,  # Format tick text
            ticklabelposition="outside",  # Position the labels outside the plot area
            tickson="labels",  # Ensure ticks are aligned with labels
            title_standoff=10,  # Increase space between x-axis title and labels
            ticks="outside",  # Ensure ticks are outside the plot area
            tickfont=dict(size=14),
        ),
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background for the plot area
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background for the whole figure
        font_color='white',
        bargap=0.4,  # Adjust the gap between bars
        bargroupgap=0.3,  # Adjust the gap between groups of bars
        yaxis=dict(
            showgrid=False  # Disable horizontal grid lines
        ),
        xaxis_title=None,
        yaxis_title=None,
    )

    # Update the layout to add border-radius effect
    fig.update_traces(marker=dict(
        line=dict(
            width=5,
            color='rgba(0,0,0,0)'  # Optional: border color
        ),
        opacity=0.9  # Optional: adjust bar opacity
    ))

    # Update legend settings
    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": -0.5,
            "xanchor": "center",
            "x": 0.5,
            "font": {
                "color": "white",  # Legend text color
                "size": 15         # Increase the font size as needed
            },
        },
        legend_title_text="",
    )

    # Convert figure to HTML and return
    fig_html = fig.to_html(include_plotlyjs='cdn')
    return fig_html


def zeniva_overview(df):
    filter_product_zin = df[df['Product'] == 'Zeniva']
    today_paid_installs = filter_product_zin['today_paid_installs'].sum()
    
    
    filter_product_zin = df[df['Product'] == 'Zeniva']
    todays_free_installs = filter_product_zin['todays_free_installs'].sum()
    
    filter_product_zin = df[df['Product'] == 'Zeniva']
    total_installs = filter_product_zin['total_installs'].sum()
    
    filter_product_zin = df[df['Product'] == 'Zeniva']
    today__paid_uninstalls = filter_product_zin['today_paid_uninstalls'].sum()
    
    filter_product_zin = df[df['Product'] == 'Zeniva']
    today_free_uninstalls = filter_product_zin['today_free_uninstalls'].sum()

    filter_product_zin = df[df['Product'] == 'Zeniva']
    total_uninstalls = filter_product_zin['total_uninstalls'].sum()

    return today_paid_installs, todays_free_installs, total_installs, today__paid_uninstalls, today_free_uninstalls, total_uninstalls


# Odyessey comparison overview part
def odyssey_overview(df):
    filter_product_zin = df[df['Product'] == 'Odyssey']
    today_forge_installs = filter_product_zin['todays_forge_installs'].sum()
    
    
    filter_product_zin = df[df['Product'] == 'Odyssey']
    todays_free_installs = filter_product_zin['todays_free_installs'].sum()
    
    filter_product_zin = df[df['Product'] == 'Odyssey']
    total_installs = filter_product_zin['total_installs'].sum()
    
    filter_product_zin = df[df['Product'] == 'Odyssey']
    today__forge_uninstalls = filter_product_zin['todays_forge_uninstalls'].sum()
    
    filter_product_zin = df[df['Product'] == 'Odyssey']
    today_free_uninstalls = filter_product_zin['today_free_uninstalls'].sum()

    filter_product_zin = df[df['Product'] == 'Odyssey']
    total_uninstalls = filter_product_zin['total_uninstalls'].sum()

    return today_forge_installs, todays_free_installs, total_installs, today__forge_uninstalls, today_free_uninstalls, total_uninstalls

def odyssey_values_for_insights():
    data = live_data.fillna(0)
    odyssey_data = data[data["product"] == "odyssey"]
    odyssey_youtube = odyssey_data[odyssey_data["platform"] == "youtube"]
    odyssey_x = odyssey_data[odyssey_data["platform"] == "x"]
    odyssey_tiktok = odyssey_data[odyssey_data["platform"] == "tiktok"]
    odyssey_instagram = odyssey_data[odyssey_data["platform"] == "instagram"]
    odyssey_facebook = odyssey_data[odyssey_data["platform"] == "facebook"]
    return (
        odyssey_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_x[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        odyssey_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )