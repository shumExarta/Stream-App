
# just for practice 



# import streamlit as st
# import pandas as pd
# from func import exarta_overview
# df  = pd.read_csv("20-9-24-Graphs_Data.csv")
# df = df.fillna(0)
# st.write(df)

# st.header("Exarta stats")
# st.markdown(
#     r"""
#     <style>
#     .stDeployButton {
#             visibility: hidden;
#         }
#     </style>
#     """, unsafe_allow_html=True
# )
# st.write(f"total followers on linkedin = {exarta_overview(df)}")

# st.header("task 1")
# # only the rows containg exarta 
# df_exarta_only = df[df['product'] == 'exarta']
# st.write(df_exarta_only)
# st.header("total followers accross all platform")
# # print(df_exarta_only)
# df_all_fol = df_exarta_only['today_followers'].sum()
# st.write(f"total followrs are {df_all_fol}")

# st.header("task 2") 
# # Filter the data for Odyssey on the PPC platform and return the rows with the relevant fields (date, clicks, daily_spend).
# df_for_ody = df.loc[(df['product'] == "odyssey") & (df['platform'] == 'ppc')].sort_values(by=["date", "clicks", "daily_spend"])
# st.write(df_for_ody)

# st.header("task 3")
# # Daily Increase in Zeniva Followers on Meta
# df_zen_day1 = df[(df['product'] == 'zeniva') & (df['platform']== 'meta') & (df['date']== '09/16/2024')]
# df_zen_day2 = df[(df['product'] == 'zeniva') & (df['platform']== 'meta') & (df['date']== '09/17/2024')]
# df_zen_day3 = df[(df['product'] == 'zeniva') & (df['platform']== 'meta') & (df['date']== '09/18/2024')]

# today_fol_for_1 = df_zen_day1['today_followers']
# today_fol_for_2 = df_zen_day1['today_followers']
# today_fol_for_3 = df_zen_day1['today_followers']

# yesterday_fol_1 = df_zen_day1['yesterday_followers']
# yesterday_fol_2 = df_zen_day1['yesterday_followers']
# yesterday_fol_3 = df_zen_day1['yesterday_followers']

# d1 = today_fol_for_1 - yesterday_fol_1
# d2 = today_fol_for_2 - yesterday_fol_2
# d3 = today_fol_for_3 - yesterday_fol_3

# st.write(f"daily incease of Zeniva on Meta on day 1 = {d1}")
# st.write(f"daily incease of Zeniva on Meta on day 2 = {d2}")
# st.write(f"daily incease of Zeniva on Meta on day 3 = {d3}")


# st.header("task 4")
# # Filter the data for Odyssey on the Shopify platform, and calculate the average daily_spend.
# df_for_ody_ppc = df[(df["product"] == "odyssey") & (df['platform'] == "shopify")]
# st.write(df_for_ody_ppc)
# st.write("Avg for dailt spend")

# df_ody_dp_1 =  df_for_ody_ppc["daily_spend"]
# sum1 = ((df_ody_dp_1).sum())
# avg = sum1/3
# st.write(f" The average daily spend is : {int(avg)}")

# st.header('task 5')

# df_ody_ti  = df[df["product"] == "odyssey"]
# daily_installs = df_ody_ti['daily_installs'].sum()
# st.write(f"total installs for odyssey are : {int(daily_installs)}")

# # making histograms
# import plotly.express as px
# data = pd.read_csv("20-9-24-Graphs_Data.csv")
# df_filled = data.fillna(0)
# # df = df_filled['views']
# # st.write(df)
# data = {"views" : [34,66,34,75,24,75,23,55,23,89,78,23,42,45],
#         'platform' : ["youtube", "meta", "facebook", "X","youtube", "meta", "facebook", "X","youtube", "meta", "facebook", "X","PPC", "x"],
#         'date': ['2024-09-10', '2024-09-11', '2024-09-12', '2024-09-10', '2024-09-11', '2024-09-11', '2024-09-10', '2024-09-12', '2024-09-11', '2024-09-11', '2024-09-12', '2024-09-11', '2024-09-10', '2024-09-10']}
# df = pd.DataFrame(data)
# fig = px.histogram(df, x = 'date',y="views", color = "platform", barmode='group',title="View by platform")
# st.write(fig)

# st.header('making a dataframe using the melt function')

# st.write(df_filled)

# data_for_melt = {
#     'date': ['2024-09-10', '2024-09-11', '2024-09-12', '2024-09-10', '2024-09-11', '2024-09-12'],
#     'platform': ['youtube', 'youtube', 'youtube', 'meta', 'meta', 'meta'],
#     'clicks': [30, 40, 50, 60, 70, 80],
#     'views': [100, 120, 150, 200, 250, 300],
#     'daily_spend': [10, 12, 15, 20, 25, 30]
# }

# df = pd.DataFrame(data_for_melt)


# df_melt = df.melt(id_vars=['date','platform'], value_vars=['clicks', 'views', 'daily_spend'],
#                   var_name='metric')

# fig2 = px.histogram(df_melt, barmode='group', x='date', y='value',facet_col='platform', color='metric', title="stats accross all platforms")

# st.write(fig2)






# def zeniva_stats_for_yt():
#     df = pd.read_csv('20-9-24-Graphs_Data.csv')
#     df=  df.fillna(0)
#     df_filtered= df[(df['product']== 'zeniva') & (df['platform']== 'youtube') ]
#     df_filtered['date']=pd.to_datetime(df_filtered['date'], format='%m/%d/%Y') 
#     df_melt = df.melt(id_vars=['date', 'product'], value_vars=['clicks', 'views', 'daily_spend'],
#                       var_name='Metric', value_name='Value')
#     fig = px.histogram(df_melt, x='date', y='Value', barmode='group', color='Metric', title="Zeniva stats on youtube")
  
#     fig.update_layout(
#         xaxis_title='Date',
#         yaxis_title='Value',
#         legend_title='Metric',
#         title_font_size=24,
#         xaxis_tickformat='%d %b', 
#         xaxis_title_standoff=10,
#         yaxis_title_standoff=10,
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         font_color='white',
#         bargap=0.5,
#         bargroupgap=0.1,
#     )
#     draw = st.write(fig)
#     return draw 
    

# zeniva_stats_for_yt()

# st.header("dataframe manipulation")
# new_df = pd.read_csv("20-9-24-Graphs_Data.csv")
# filled_data = new_df.fillna(0)
# st.write(filled_data)


# all_cols  = filled_data.columns.to_list()
# print(all_cols)

# df_daily_spend_higher_than_1000 = filled_data[filled_data['daily_spend'] > 5000].sort_values(by=['product', 'platform', 'date', 'clicks', 'daily_spend', 'views', 'impressions'])



# st.write(df_daily_spend_higher_than_1000)