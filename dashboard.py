import streamlit as st
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

import altair as alt

alt.themes.enable("default")
# Set Nunito as font for the plot
def nunito_theme():
    return {
        "config": {
            "title": {
                "font": "Nunito Sans",
            },
            "axis": {
                "labelFont": "Nunito Sans",
                "titleFont": "Nunito Sans",
            },
            "legend": {
                "labelFont": "Nunito Sans",
                "titleFont": "Nunito Sans",
            }
        }
    }

alt.themes.register("nunito_theme", nunito_theme)
alt.themes.enable("nunito_theme")

df_melted = df.melt(id_vars=["Date"], value_vars=[f"Series_{i+1}" for i in range(10)], 
                    var_name="Series", value_name="Value")

chart = alt.Chart(df_melted).mark_line().encode(
    x="Date:T",
    y="Value:Q",
    color=alt.Color("Series:N", scale=alt.Scale(domain=[f"Series_{i+1}" for i in range(10)], range=colors)),
    tooltip=["Date", "Value", "Series"]
).properties(
    width=600,
    height=400,
    title="Multiple Time Series"
).interactive()

st.altair_chart(chart)

# Set Nunito as font for the plot
def nunito_theme():
    return {
        "config": {
            "title": {
                "font": "Nunito Sans",
                "fontSize": 20
            },
            "axis": {
                "labelFont": "Nunito Sans",
                "labelFontSize": 14,
                "titleFont": "Nunito Sans",
                "titleFontSize": 16
            },
            "legend": {
                "labelFont": "Nunito Sans",
                "labelFontSize": 12,
                "titleFont": "Nunito Sans",
                "titleFontSize": 14
            },
            "header": {
                "labelFont": "Nunito Sans",
                "titleFont": "Nunito Sans",
            }
        }
    }

alt.themes.register("nunito_theme", nunito_theme)
alt.themes.enable("nunito_theme")

chart = alt.Chart(df_melted).mark_line().encode(
    x="Date:T",
    y="Value:Q",
    color=alt.Color("Series:N", scale=alt.Scale(domain=[f"Series_{i+1}" for i in range(10)], range=colors)),
    tooltip=["Date", "Value", "Series"]
).properties(
    width=1200,  # Adjusted width
    height=400,
    title="Multiple Time Series"
).interactive()

st.altair_chart(chart)


from st_aggrid import AgGrid

# Generate sample data
np.random.seed(42)
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": np.random.randint(1000, 5000, 5),
    "Profit": np.random.randint(100, 1000, 5)
}
df = pd.DataFrame(data)

# Define grid options for ag-grid customization
gridOptions = {
    'defaultColDef': {
        'sortable': True, 
        'filter': True,
        'resizable': True,
    },
    'columnDefs': [
        {'headerCheckboxSelection': True, 'checkboxSelection': True, 'width': 50, 'suppressSizeToFit': True, 'headerCheckboxSelectionFilteredOnly': True},
        {'headerName': 'Product', 'field': 'Product'},
        {'headerName': 'Sales', 'field': 'Sales'},
        {'headerName': 'Profit', 'field': 'Profit'}
    ],
    'rowSelection': 'multiple',
    'domLayout': 'autoHeight'
}

# Define colors
HEADER_COLOR = "#cfcfcf"
TEXT_COLOR = "#746c64"
BACKGROUND_COLOR = "#f0e9e6"

# Apply CSS styles
st.markdown(f"""
    <style>
        .ag-header-cell {{
            background-color: {HEADER_COLOR};
            color: {TEXT_COLOR};
            font-family: Nunito, sans-serif;
            font-size: 16px;
        }}
        .ag-cell {{
            font-family: Nunito, sans-serif;
            font-size: 14px;
            color: {TEXT_COLOR};
            border-right: 1px solid #ddd;
        }}
        .ag-root {{
            background-color: {BACKGROUND_COLOR};
        }}
    </style>
""", unsafe_allow_html=True)

# Display the title and the table

AgGrid(df, gridOptions=gridOptions, height=400, width="50%", fit_columns_on_grid_load=True)

# Generate sample data
np.random.seed(42)
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": np.random.randint(1000, 5000, 5),
    "Profit": np.random.randint(100, 1000, 5)
}
df = pd.DataFrame(data)

# Define grid options for ag-grid customization
gridOptions = {
    'defaultColDef': {
        'sortable': True, 
        'filter': True,
        'resizable': True,
    },
    'columnDefs': [
        {'headerName': 'Product', 'field': 'Product'},
        {'headerName': 'Sales', 'field': 'Sales'},
        {'headerName': 'Profit', 'field': 'Profit'}
    ],
    'domLayout': 'autoHeight'
}

# Define colors
HEADER_COLOR = "#d7d0cd"  # Sandy Grey from the provided palette
TEXT_COLOR = "#746c64"
BACKGROUND_COLOR = "#f0e9e6"

# Apply CSS styles
st.markdown(f"""
    <style>
        .ag-header-cell {{
            background-color: {HEADER_COLOR};
            color: {TEXT_COLOR};
            font-family: 'Nunito', sans-serif;
            font-size: 16px;
        }}
        .ag-cell {{
            font-family: 'Nunito', sans-serif;
            font-size: 14px;
            color: {TEXT_COLOR};
            border-right: 1px solid #ddd;
        }}
        .ag-root {{
            background-color: {BACKGROUND_COLOR};
        }}
    </style>
""", unsafe_allow_html=True)

# Display the title and the table
st.title("Refined Elegant Data Table with Streamlit AgGrid")
AgGrid(df, gridOptions=gridOptions, height=400, width="100%", fit_columns_on_grid_load=True)

# Generate sample data
np.random.seed(42)
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": np.random.randint(1000, 5000, 5),
    "Profit": np.random.randint(100, 1000, 5)
}
df = pd.DataFrame(data)

# "Table" aesthetics
HEADER_COLOR = "#d7d0cd"
TEXT_COLOR = "#746c64"

# Creating a base for our "table"
base = alt.Chart(df).encode(
    y=alt.Y('Product:N', axis=alt.Axis(orient='right')),
)

# "Columns" in our table
sales = base.mark_text(align='left').encode(
    text=alt.Text('Sales:Q', format=','),
    x=alt.value(20),  # pixels from the left side
    color=alt.value(TEXT_COLOR)
)

profit = base.mark_text(align='left').encode(
    text='Profit:Q',
    x=alt.value(200),  # pixels from the left side
    color=alt.value(TEXT_COLOR)
)

# Background color for header
header_bg = alt.Chart(pd.DataFrame([{}])).mark_rect().encode(
    x=alt.value(0), x2=alt.value(400),
    y=alt.value(0), y2=alt.value(20),
    color=alt.value(HEADER_COLOR)
)

# Header text
header = alt.Chart(pd.DataFrame({
    'Function': ['Sales', 'Profit'],
    'x': [50, 225],
})).mark_text(color=TEXT_COLOR, fontSize=15).encode(
    x='x:Q',
    y=alt.value(15),
    text='Function:N'
)

# Combine everything
table = (header_bg + header + sales + profit).configure_view(strokeWidth=0)

st.title("Altair Table Visualization")
st.write(table)

