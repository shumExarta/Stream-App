import pandas as pd
import streamlit as st
import plotly.express as px

live_data = pd.read_csv("graph_data_final.csv")


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
    

def odyessey_values_for_insights():
    data = live_data.fillna(0)
    odyessey_data = data[data["product"] == "odyessey"]
    odyessey_youtube = odyessey_data[odyessey_data["platform"] == "youtube"]
    odyessey_x = odyessey_data[odyessey_data["platform"] == "x"]
    odyessey_tiktok = odyessey_data[odyessey_data["platform"] == "tiktok"]
    odyessey_instagram = odyessey_data[odyessey_data["platform"] == "instagram"]
    odyessey_facebook = odyessey_data[odyessey_data["platform"] == "facebook"]
    return (
        odyessey_youtube[["total_followers", "today_followers", "yesterday_followers"]],
        odyessey_x[["total_followers", "today_followers", "yesterday_followers"]],
        odyessey_tiktok[["total_followers", "today_followers", "yesterday_followers"]],
        odyessey_instagram[["total_followers", "today_followers", "yesterday_followers"]],
        odyessey_facebook[["total_followers", "today_followers", "yesterday_followers"]],
    )
    

def exarta_values_for_insights():
    data = live_data.fillna(0)
    exarta_data = data[data["product"] == "odyessey"]
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
    df = pd.read_csv('graph_data_final.csv')
    df = df.fillna(0)
    df = df[df['product'] == product_name]
    
    platform_metrics = {
        'youtube': ['clicks', 'views', 'daily_spend'],
        'meta': ['clicks', 'reach', 'daily_spend'],
        'shopify': ['clicks', 'daily_spend'],
        'ppc': ['clicks', 'daily_spend', 'impressions'],
    }
    
    if platform_name in platform_metrics:
        selected_metrics = platform_metrics[platform_name]
    else:
        st.error(f"Platform {platform_name} not recognised.")
        return
    
    df_platform = df[df['platform'] == platform_name]
    df_grouped = df_platform[['date'] + selected_metrics].melt(id_vars='date', var_name='Metric', value_name='Value')
    
    color_discrete_map = {
        'clicks': '#BC679C',
        'views': '#F68C5B',
        'daily_spend': '#A6B174',
        'reach': '#8567BC',
        'impressions': '#F68C5B'
    }
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
    
    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background for the plot area
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background for the whole figure,
    font_color='white'
    )
    
    fig.update_layout(
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': -0.3,  
            'xanchor': 'center',
            'x': 0.5,    
            'font': {
            'color': 'white'  # Legend text color
        }
        },
        xaxis_title=None,
        yaxis_title=None,
        legend_title_text='',  
    )
    
    fig_html = fig.to_html(include_plotlyjs='cdn')

    # Render the HTML in Streamlit
    return fig_html