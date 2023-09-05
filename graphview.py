

##### Simulated data section

import pandas as pd
import numpy as np
import random
import os
import igraph as ig
from tqdm import tqdm  # For progress bars


### Data Generation
def generate_fake_data(start_yearmonth, end_yearmonth, num_companies=100, base_num_transactions=1000):
    # Convert YYYYMM string to datetime
    start_date = pd.to_datetime(start_yearmonth, format='%Y%m')
    end_date = pd.to_datetime(end_yearmonth, format='%Y%m')

    # Generate company names
    #companies = ["Company_" + str(i) for i in range(1, num_companies + 1)]
    companies = [str(i) for i in range(1, num_companies + 1)]
    major_players = companies[:num_companies // 10]  # Top 10% are major players

    all_transactions = []

    current_date = start_date
    while current_date <= end_date:
        # Introduce variability in number of transactions per month
        month_multiplier = random.uniform(0.8, 1.2)
        num_transactions = int(base_num_transactions * month_multiplier)

        for _ in range(num_transactions):
            is_major = random.choice([True, False, False])  # 1 in 3 chance
            if is_major:
                company_origin = random.choice(major_players)
                company_destiny = random.choice(major_players)
            else:
                company_origin = random.choice(companies)
                company_destiny = random.choice(companies)
            while company_origin == company_destiny:
                company_destiny = random.choice(companies)

            # Generate transaction volume based on power-law distribution
            volume = int((np.random.power(a=0.1) + 0.1) * 10000)  # Modify 0.1 and 10000 as per required scale
            
            yearmonth = current_date.strftime('%Y%m')
            all_transactions.append([yearmonth, company_origin, company_destiny, volume])

        # Move to the next month
        current_date = current_date + pd.DateOffset(months=1)

    # Create a DataFrame
    df = pd.DataFrame(all_transactions, columns=['yearmonth', 'company_origin', 'company_destiny', 'volume'])

    return df

# Generate the fake data
#fake_data = generate_fake_data(start_yearmonth="202201", end_yearmonth="202312", num_companies=100, base_num_transactions=12000)


### File Simulation

def generate_network_features_for_month(data):
    # Create an igraph Graph from the data
    g = ig.Graph.TupleList(data[['company_origin', 'company_destiny', 'volume']].itertuples(index=False), directed=True, edge_attrs=['volume'])
    
    # Calculate graph features
    in_degrees = g.degree(mode="in")
    out_degrees = g.degree(mode="out")
    strengths_in = g.strength(weights="volume", mode="in")
    strengths_out = g.strength(weights="volume", mode="out")
    eigenvector_centralities = g.eigenvector_centrality(directed=True, weights="volume")
    #clustering_coefficients = g.transitivity_local_undirected(mode="zero", weights="volume")

    # Convert to DataFrame
    df = pd.DataFrame({
        'company': g.vs["name"],
        'in_degree': in_degrees,
        'out_degree': out_degrees,
        'strength_in': strengths_in,
        'strength_out': strengths_out,
        'eigenvector_centrality': eigenvector_centralities,
        #'clustering_coefficient': clustering_coefficients
    })
    
    return df

def generate_feature_files(fake_data):
    months = fake_data['yearmonth'].unique()
    
    for month in tqdm(months):  # tqdm provides a progress bar
        month_data = fake_data[fake_data['yearmonth'] == month]
        feature_df = generate_network_features_for_month(month_data)
        
        # Save the dataframe to CSV
        file_name = f"simul_{month}.csv"
        feature_df.to_csv(file_name, index=False)

# Generate the feature files
#generate_feature_files(fake_data)


def consolidate_files(prefix, directory_path):
    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Filter files by the _YYYYMM extension
    valid_files = [f for f in files if prefix in f]

    if not valid_files:
        raise ValueError("No valid files found in the provided directory")

    # Extract the common prefix
    common_prefix = os.path.commonprefix(valid_files)

    # Initiate an empty DataFrame to append data
    consolidated_df = pd.DataFrame()

    # Process each valid file
    for file in valid_files:
        file_path = os.path.join(directory_path, file)
        temp_df = pd.read_csv(file_path)

        # Extract YYYY-MM from the file's extension and create a 'safra' column
        year_month = file[-7:-3] + "-" + file[-2:]
        #temp_df['safra'] = pd.to_datetime(year_month, format='%Y-%m')
        
        # Append the data to the consolidated DataFrame
        consolidated_df = consolidated_df.append(temp_df, ignore_index=True)

    # Save the consolidated DataFrame as Parquet
    consolidated_df.to_parquet(os.path.join(directory_path, prefix + ".parquet"), index=False)


# Call the function
#directory_path = os.getcwd()
#prefix = 'simul'
#consolidate_files(prefix,directory_path)

import streamlit as st
import pandas as pd
import altair as alt
import glob

# --- CSS and Setup ---
# ... (All your CSS and setup code comes here) ...

# Load data
def load_data():
    files = glob.glob("simul_*.csv")
    dfs = [pd.read_csv(file) for file in files]
    
    # Consolidate into a single dataframe
    data = pd.concat(dfs, ignore_index=True)
    data['safra'] = pd.to_datetime(data['safra'])
    return data

df = load_data()

# Multi-select for companies
companies = df['company'].unique().tolist()
selected_companies = st.multiselect('Select Companies', companies)

# Single select for metric
metrics = ['in_degree', 'out_degree', 'strength_in', 'strength_out', 'eigenvector_centrality', 'clustering_coefficient']
selected_metric = st.selectbox('Select Metric', metrics)

# Filter data based on selected companies and metric
filtered_df = df[df['company'].isin(selected_companies)][['safra', 'company', selected_metric]]

# Plot with Altair
chart = alt.Chart(filtered_df).mark_line().encode(
    x="safra:T",
    y=alt.Y(f"{selected_metric}:Q", title=selected_metric),
    color="company:N",
    tooltip=["safra", "company", selected_metric]
).properties(
    width=1200,
    height=400,
    title=f"Time Series of {selected_metric}"
).interactive()

st.altair_chart(chart)

import streamlit as st
import pandas as pd
import altair as alt
import glob
from sklearn.preprocessing import MinMaxScaler

mport streamlit as st
from streamlit.components.v1 import html
st.set_page_config(layout="wide")
st.markdown(
            f'''
<style>
.appview-container .main .block-container{{
        padding-top: -1rem; 
        padding-left: 0.1rem;
        padding-right: 0.1rem}}
</style>
            ''',unsafe_allow_html=True)
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''

st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


st.image('itaubbaheader.png',use_column_width=True)

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .big-font {
            font-family: 'Nunito', sans-serif;
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">Acompanhamento de métricas </div>', unsafe_allow_html=True)

import pandas as pd
import numpy as np

np.random.seed(42)
date_range = pd.date_range(start="2022-01-01", periods=100, freq="D")
data = {
    "Date": date_range,
}
colors = ["#cfcfcf", "#746c64", "#ec7506", "#f3a45b", "#9ba7b4", "#0c1433", "#d1a969", "#d7d0cd", "#f0e9e6", "#444c44"]

for i, color in enumerate(colors):
    data[f"Series_{i+1}"] = np.random.randn(100).cumsum()

df = pd.DataFrame(data)


# Load data
def load_data():
    files = glob.glob("simul_*.csv")
    dfs = [pd.read_csv(file) for file in files]
    
    # Consolidate into a single dataframe
    data = pd.concat(dfs, ignore_index=True)
    data['safra'] = pd.to_datetime(data['safra'])
    return data

df = load_data()

# Multi-select for companies
companies = df['company'].unique().tolist()
selected_companies = st.multiselect('Select Companies for Single Feature Visualization', companies)

# Single select for metric
metrics = ['in_degree', 'out_degree', 'strength_in', 'strength_out', 'eigenvector_centrality', 'clustering_coefficient']
selected_metric = st.selectbox('Select Metric', metrics)

# Filter data based on selected companies and metric
filtered_df = df[df['company'].isin(selected_companies)][['safra', 'company', selected_metric]]

# Plot multiple companies for a single feature with Altair
chart1 = alt.Chart(filtered_df).mark_line().encode(
    x="safra:T",
    y=alt.Y(f"{selected_metric}:Q", title=selected_metric),
    color="company:N",
    tooltip=["safra", "company", selected_metric]
).properties(
    width=1200,
    height=400,
    title=f"Time Series of {selected_metric} for Selected Companies"
).interactive()

st.altair_chart(chart1)

# --- Visualization for a Single Company with All Features ---

# Single select for one company
selected_single_company = st.selectbox('Select Company for Multi Feature Visualization', companies)

# Filter data for selected company
single_company_df = df[df['company'] == selected_single_company]

# Normalize features for the selected company
scaler = MinMaxScaler()
features_df = single_company_df[metrics]
scaled_features = scaler.fit_transform(features_df)
scaled_df = pd.DataFrame(scaled_features, columns=features_df.columns)
scaled_df['safra'] = single_company_df['safra'].values

# Melt the dataframe for Altair visualization
melted_df = scaled_df.melt(id_vars=['safra'], value_vars=metrics)

# Plot all features for a single company with Altair
chart2 = alt.Chart(melted_df).mark_line().encode(
    x="safra:T",
    y=alt.Y("value:Q", title="Normalized Value"),
    color="variable:N",
    tooltip=["safra", "value", "variable"]
).properties(
    width=1200,
    height=400,
    title=f"Normalized Time Series of All Features for {selected_single_company}"
).interactive()

st.altair_chart(chart2)