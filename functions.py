import pandas as pd

def histo_youtube(dataframe):
    df_youtube = dataframe[dataframe['platform'] == 'youtube']
    youtube_melted = df_youtube.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    
    df_meta = dataframe[dataframe['platform'] == 'meta']
    meta_melted = df_meta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
        
    return youtube_melted, meta_melted


def filtering_data(dataframe):
    # FOR EXARTA
    filter_product_exarta = dataframe[dataframe['product'] == 'exarta']
    
    # FOR EXARTA YOUTUBE
    filter_youtube_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'youtube']
    youtube_melted = filter_youtube_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA META
    filter_meta_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'meta']
    meta_melted = filter_meta_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA PPC
    filter_ppc_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'ppc']
    ppc_melted = filter_ppc_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    
    return youtube_melted, meta_melted, ppc_melted