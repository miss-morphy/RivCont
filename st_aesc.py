import streamlit as st
from streamlit.components.v1 import html
# Set page config for wider display and title
st.set_page_config(page_title="Streamlit App", layout="wide")

st.markdown("""
    <style>
        /* Remove default Streamlit paddings */
        .reportview-container {
            padding: 0 !important;
        }
        .stApp {
            margin: 0 !important;
        }
        
        /* Adjust logo margin */
        img {
            margin-bottom: 0.5rem !important;
        }

        /* Style for the line */
        hr {
            margin-top: 0 !important;
            margin-bottom: 1rem !important;
            border-color: #3a3a3a !important;
            border-width: 0.3px !important;
        }

        /* Font styles */
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100&display=swap');
        h1, h2 {
            font-family: 'Lato', sans-serif !important;
            font-weight: 100 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
            f'''
<style>
.appview-container .main .block-container{{
        padding-top: 0rem; 
        padding-left: 2.1rem;
        padding-right: 2.1rem}}
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

#st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Display the logo from the current folder
st.image('jccb_logo.png',width = 111)

# Display a very thin, more distant from black line right below the logo
st.markdown("""
    <hr style="margin-top: 0rem; margin-bottom: 0rem; border-color: #3a3a3a; border-width: 0.2px;">
""", unsafe_allow_html=True)

# Use HTML to reference Google Fonts
# I've selected "Lato" with weight `100` which is a thin, elegant font suitable for professional use.
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100&display=swap');
        h1, h2 {
            font-family: 'Lato', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# Display titles and subtitles with thin fonts
st.markdown("<h1>Title</h1>", unsafe_allow_html=True)
st.markdown("<h2>Subtitle</h2>", unsafe_allow_html=True)

import pandas as pd

# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google'],
    'Revenue': [274.5, 115.6, 143.0, 181.7],
    'Profit': [57.4, 29.1, 44.3, 40.3]
}
df = pd.DataFrame(data)

# Display data
selected_company = st.session_state.get('selected_company', None)
if selected_company:
    st.write(df[df['Company'] == selected_company])
else:
    st.write(df)

# Custom HTML for filter
html_filter = """
    <style>
        select {
            font-family: 'Lato', sans-serif;
            font-weight: 100;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #3a3a3a;
        }
    </style>

    <label for="company">Choose a company:</label>
    <select name="company" id="companyDropdown">
      <option value="all">All</option>
      <option value="Apple">Apple</option>
      <option value="JP Morgan">JP Morgan</option>
      <option value="Microsoft">Microsoft</option>
      <option value="Google">Google</option>
    </select>

    <script>
        const dropdown = document.getElementById('companyDropdown');
        dropdown.onchange = (event) => {
            const selectedValue = event.target.value;
            if (selectedValue === "all") {
                window.parent.postMessage({type: "streamlit", method: "setSessionState", args: {selected_company: null}}, "*");
            } else {
                window.parent.postMessage({type: "streamlit", method: "setSessionState", args: {selected_company: selectedValue}}, "*");
            }
        }
    </script>
"""

html(html_filter, width=300, height=100)


# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google'],
    'Revenue': [274.5, 115.6, 143.0, 181.7],
    'Profit': [57.4, 29.1, 44.3, 40.3]
}
df = pd.DataFrame(data)

# Custom HTML for filter
html_filter = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100&display=swap');

        body, select, label {
            font-family: 'Lato', sans-serif;
            font-weight: 100;
        }

        select {
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #3a3a3a;
            margin-left: 10px;
        }
    </style>

    <label for="company">Choose a company:</label>
    <select name="company" id="companyDropdown">
      <option value="all">All</option>
      <option value="Apple">Apple</option>
      <option value="JP Morgan">JP Morgan</option>
      <option value="Microsoft">Microsoft</option>
      <option value="Google">Google</option>
    </select>

    <script>
        const dropdown = document.getElementById('companyDropdown');
        dropdown.onchange = (event) => {
            const selectedValue = event.target.value;
            if (selectedValue === "all") {
                window.parent.postMessage({type: "streamlit", method: "setSessionState", args: {selected_company: null}}, "*");
            } else {
                window.parent.postMessage({type: "streamlit", method: "setSessionState", args: {selected_company: selectedValue}}, "*");
            }
        }
    </script>
"""

st.components.v1.html(html_filter, width=400, height=100)


# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google', 'Facebook'],
    'Revenue': [274.5, 115.6, 143.0, 181.7, 85.9],
    'Profit': [57.4, 29.1, 44.3, 40.3, 29.1]
}
df = pd.DataFrame(data)

# Lato font for better aesthetics (using markdown)
st.markdown("<style>body {font-family: 'Lato', sans-serif;}</style>", unsafe_allow_html=True)

# Filters
companies = ['All'] + list(df['Company'])
selected_company = st.selectbox("Choose a company", companies, format_func=lambda x: 'All' if x == 'All' else x)

multiselect_companies = st.multiselect("Choose multiple companies", companies, default='All')

if selected_company != 'All':
    df = df[df['Company'] == selected_company]

if 'All' not in multiselect_companies and len(multiselect_companies) > 0:
    df = df[df['Company'].isin(multiselect_companies)]

st.write(df)

# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google', 'Facebook'],
    'Revenue': [274.5, 115.6, 143.0, 181.7, 85.9],
    'Profit': [57.4, 29.1, 44.3, 40.3, 29.1]
}
df = pd.DataFrame(data)

# Embed Lato font and apply it
font_code = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100;300&display=swap');
    body {
        font-family: 'Lato', sans-serif;
    }
    div[role="listbox"] ul {
        background-color: #3A539B !important;  /* This will change dropdown background color */
    }
</style>
"""
st.markdown(font_code, unsafe_allow_html=True)

# Using Lato font for text but Streamlit's widgets for the filter
st.markdown("<h2 style='font-family:lato;color:#3A539B'>Choose a company</h2>", unsafe_allow_html=True)
companies = ['All'] + list(df['Company'])
selected_company = st.selectbox("", companies, format_func=lambda x: 'All' if x == 'All' else x, index=0)

if selected_company != 'All':
    df = df[df['Company'] == selected_company]

st.write(df)


import streamlit as st
import pandas as pd

# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google', 'Facebook'],
    'Revenue': [274.5, 115.6, 143.0, 181.7, 85.9],
    'Profit': [57.4, 29.1, 44.3, 40.3, 29.1]
}
df = pd.DataFrame(data)

# Custom HTML filter for single select
html_single_select = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100&display=swap');
        body, select, label {
            font-family: 'Lato', sans-serif;
            font-weight: 100;
            color: #3A539B;
            font-size: 16px;
        }
        select {
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #3a3a3a;
            margin-left: 10px;
            background-color: #FF8C42;
            color: white;
        }
    </style>
    <label for="company">Choose a company:</label>
    <select name="company" id="companyDropdown">
      <option value="all">All</option>
      <option value="Apple">Apple</option>
      <option value="JP Morgan">JP Morgan</option>
      <option value="Microsoft">Microsoft</option>
      <option value="Google">Google</option>
    </select>
"""

# Custom HTML filter for multi select
html_multi_select = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100&display=swap');
        body, select, label {
            font-family: 'Lato', sans-serif;
            font-weight: 100;
            color: #3A539B;
            font-size: 16px;
        }
        select {
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #3a3a3a;
            margin-left: 10px;
            background-color: #3A539B;
            color: white;
        }
    </style>
    <label for="companies">Choose companies (Ctrl/Command to select multiple):</label>
    <select multiple name="companies" id="companyMultiDropdown">
      <option value="all">All</option>
      <option value="Apple">Apple</option>
      <option value="JP Morgan">JP Morgan</option>
      <option value="Microsoft">Microsoft</option>
      <option value="Google">Google</option>
    </select>
"""

st.markdown(html_single_select, unsafe_allow_html=True)
st.markdown(html_multi_select, unsafe_allow_html=True)
# Rest of the code for data display
st.write(df)

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Generate a sample DataFrame
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
df = pd.DataFrame({
    'x': np.tile(np.arange(1, 6), 7),
    'y': np.random.rand(35) + np.repeat(np.arange(7), 5),
    'Category': np.repeat(categories, 5)
})
df = pd.DataFrame(df)

# Altair chart
colors = ['#000000', '#EC7506', '#0C1433', '#F3A45B', '#7D9CC0', '#444C44', '#746c64']

# Define a custom theme
def custom_theme():
    return {
        "config": {
            "title": {
                "font": "Lato",
                "fontSize": 16
            },
            "axisX": {
                "grid": False,
                "labelFont": "Lato",
                "labelFontSize": 12,
                "titleFont": "Lato",
                "titleFontSize": 12
            },
            "axisY": {
                "gridColor": "#ddd",  # A soft grid color
                "gridWidth": 0.5,
                "labelFont": "Lato",
                "labelFontSize": 12,
                "labelAlign": "left",
                "titleFont": "Lato",
                "titleFontSize": 12,
                "titlePadding": 10,  # Adjusts the distance of the y-title from axis
            },
            "header": {
                "labelFont": "Lato",
                "titleFont": "Lato"
            },
            "legend": {
                "labelFont": "Lato",
                "titleFont": "Lato"
            },
            "line": {
                "strokeWidth": 2.5
            }
        }
    }
# Register and enable the custom theme
alt.themes.register('custom_theme', custom_theme)
alt.themes.enable('custom_theme')

# Set the default font to Lato
#alt.themes.enable('default')
#alt.themes.configure_theme('default', font='Lato')

# Filters
st.markdown("<div style='font-family:lato;color:#4A4A4A;font-size:14px;margin-bottom:0px;'>Choose a category</div>", unsafe_allow_html=True)
selected_category = st.selectbox("", ['All'] + categories, index=0)

st.markdown("<div style='font-family:lato;color:#4A4A4A;font-size:14px;margin-top:20px;margin-bottom:0px;'>Choose multiple categories</div>", unsafe_allow_html=True)
selected_categories = st.multiselect("", categories, default=categories)

if selected_category != 'All':
    df = df[df['Category'] == selected_category]
else:
    df = df[df['Category'].isin(selected_categories)]

# Chart Creation
chart = alt.Chart(df).mark_line().encode(
    x=alt.X("x:Q", axis=alt.Axis(title="X Axis")),
    y=alt.Y("y:Q", axis=alt.Axis(title="Y Axis", titleAlign="right")),
    color="category:N"
).properties(width=600, height=400)

chart = chart.configure_axisRight(labelAlign='left')

st.altair_chart(chart)
st.altair_chart(chart, use_container_width=True)

# Simulate a DataFrame
data = {
    'Company': ['Apple', 'JP Morgan', 'Microsoft', 'Google', 'Facebook'],
    'Revenue': [274.5, 115.6, 143.0, 181.7, 85.9],
    'Profit': [57.4, 29.1, 44.3, 40.3, 29.1]
}
df = pd.DataFrame(data)

# Embed Lato font and adjust margins
font_code = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@100;300&display=swap');

    /* Override Streamlit's default styles for spacing */
    div.row-widget.stSelectbox > div, div.row-widget.stMultiselect > div {
        margin-top: -15px;
    }
</style>
"""
st.markdown(font_code, unsafe_allow_html=True)

# Use HTML to render the label in Lato font with a smaller size and a neutral dark gray color
st.markdown("<div style='font-family:lato;color:#4A4A4A;font-size:14px;margin-bottom:0px;'>Choose a company</div>", unsafe_allow_html=True)
selected_company = st.selectbox("    ", ['All'] + list(df['Company']), index=0)

st.markdown("<div style='font-family:lato;color:#4A4A4A;font-size:14px;margin-bottom:0px;'>Choose multiple companies</div>", unsafe_allow_html=True)
selected_companies = st.multiselect("     ", ['All'] + list(df['Company']))

if selected_company != 'All':
    df = df[df['Company'] == selected_company]

st.write(df)

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-01-05", freq='D')
df = pd.DataFrame({
    'date': np.tile(date_range, 7),
    'value': np.random.rand(35) + np.repeat(np.arange(7), 5),
    'category': np.repeat(categories, 5)
})


# Defining, registering, and enabling the custom theme
def economist_theme():
    font = "Lato"
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    markColor = "#0C1433"
    textColor = "#000000"
    
    return {
        "config": {
            "title": {
                "fontSize": 24,
                "font": font,
                "anchor": "start",
                "color": textColor
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "tickColor": axisColor,
                "tickSize": 5,
                "titleFont": font,
                "titleFontSize": 16,
                "titlePadding": 10,
                "title": "X Axis",
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "ticks": False,
                "titleFont": font,
                "titleFontSize": 16,
                "titleAngle": 0,
                "titleY": -10,
                "titleX": -60,
            },
            "background": "transparent",
            "line": {
                "stroke": markColor,
                "strokeWidth": 2,
            },
            "view": {
                "stroke": "transparent",
            },
        }
    }

# Register and enable the custom theme
alt.themes.register('economist_theme', economist_theme)
alt.themes.enable('economist_theme')

color_palette = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

chart = alt.Chart(df).mark_line().encode(
    x=alt.X("date:T", axis=alt.Axis(title="Date")),
    y=alt.Y("value:Q", axis=alt.Axis(title="Value")),
    color=alt.Color("category:N", scale=alt.Scale(range=color_palette))
).properties(width=600, height=400)

st.altair_chart(chart, use_container_width = True)

# Simulating data
np.random.seed(42)

np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='D')
df = pd.DataFrame({
    'date': np.tile(date_range, 7),
    'value': np.random.rand(7 * len(date_range)) + np.repeat(np.arange(7), len(date_range)),
    'category': np.repeat(categories, len(date_range))
})

# Defining, registering, and enabling the custom theme
def economist_theme():
    font = "Lato"
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    
    return {
        "config": {
            "title": {
                "fontSize": 16,
                "font": font,
                "anchor": "start",
                "color": axisColor
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "tickColor": axisColor,
                "tickSize": 5,
                "titleFont": font,
                "titleFontSize": 14,
                "titlePadding": 10,
                "format": "%b %Y"
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "ticks": False,
                "titleFont": font,
                "titleFontSize": 14,
                "titleAngle": 0,
                "titleY": -10,
                "titleX": -60,
            },
            "background": "transparent",
            "line": {
                "strokeWidth": 2,
            },
            "legend": {
                "labelFont": font,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 14,
            },
            "view": {
                "stroke": "transparent",
            },
        }
    }

# Register and enable the custom theme
alt.themes.register('economist_theme', economist_theme)
alt.themes.enable('economist_theme')

color_palette = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

chart = alt.Chart(df).mark_line().encode(
    x=alt.X("date:T", axis=alt.Axis(title="Date")),
    y=alt.Y("value:Q", axis=alt.Axis(title="Value", orient='right')),
    color=alt.Color("category:N", scale=alt.Scale(range=color_palette), legend=alt.Legend(title="Category"))
).properties(width=600, height=400, title="Multiline Chart Overview")

st.altair_chart(chart)

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='D')
df = pd.DataFrame({
    'date': np.tile(date_range, 7),
    'value': np.random.rand(7 * len(date_range)) + np.repeat(np.arange(7), len(date_range)),
    'category': np.repeat(categories, len(date_range))
})

# Defining, registering, and enabling the custom theme
def economist_theme():
    font = "Lato"
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    
    return {
        "config": {
            "title": {
                "fontSize": 16,
                "font": font,
                "anchor": "start",
                "color": axisColor
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "tickColor": axisColor,
                "tickSize": 5,
                "titleFont": font,
                "titleFontSize": 14,
                "titlePadding": 10,
                "format": "%b %Y"
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0,
                "ticks": False,
                "titleFont": font,
                "titleFontSize": 14,
                "titleAngle": 0,
                "titleY": -10,
                "titleX": -60,
            },
            "background": "transparent",
            "line": {
                "strokeWidth": 2,
            },
            "legend": {
                "labelFont": font,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 14,
            },
            "view": {
                "stroke": "transparent",
            },
        }
    }

# Register and enable the custom theme
alt.themes.register('economist_theme', economist_theme)
alt.themes.enable('economist_theme')

color_palette = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

chart = alt.Chart(df).mark_line().encode(
    x=alt.X("date:T", axis=alt.Axis(title="Date")),
    y=alt.Y("value:Q", axis=alt.Axis(title="Value", orient='right')),
    color=alt.Color("category:N", scale=alt.Scale(range=color_palette), legend=alt.Legend(title="Category"))
).properties(width=600, height=400, title="Multiline Chart Overview")

st.altair_chart(chart)

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='D')
df = pd.DataFrame({
    'date': np.tile(date_range, 7),
    'value': np.random.rand(7 * len(date_range)) + np.repeat(np.arange(7), len(date_range)),
    'category': np.repeat(categories, len(date_range))
})

# Altair chart
alt.themes.register('my_custom_theme', lambda: {
    "config": {
        "title": {
            "fontSize": 20,
            "font": "Lato",
            "anchor": "start",
        },
        "axis": {
            "titleFont": "Lato",
            "labelFont": "Lato",
            "grid": True,
            "gridColor": "#ddd",
            "gridWidth": 0.5,
            "domain": False,
            "tickBand": "extent"
        },
        "legend": {
            "titleFont": "Lato",
            "labelFont": "Lato"
        },
        "header": {
            "titleFont": "Lato",
            "labelFont": "Lato"
        }
    }
})

alt.themes.enable('my_custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='', axis=alt.Axis(titleAngle=0, titleAlign='left', titleY=-20, titleX=-45)),
    color='category:N',
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title="Multiline Chart"
).configure_axisY(
    titleAngle=0,
    titleY=-40,
    titleX=30
)

st.write(chart)

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='D')
df = pd.DataFrame({
    'date': np.tile(date_range, 7),
    'value': np.random.rand(7 * len(date_range)) + np.repeat(np.arange(7), len(date_range)),
    'category': np.repeat(categories, len(date_range))
})

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'title': {'font': 'Lato', 'fontSize': 20, 'anchor': 'start'},
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title=None, axis=alt.Axis(titleAngle=0, titleAlign='left', titleY=-20, titleX=-45, labels=True, ticks=False)),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title="Multiline Chart"
).configure_axisY(
    titleAngle=0,
    titleY=-40,
    titleX=30
)

st.write(chart)

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='M')
values = np.random.randn(len(date_range) * 7).cumsum().reshape((len(date_range), 7)) + np.arange(7) * 10
df = pd.DataFrame(values, columns=categories)
df['date'] = date_range

df = df.melt(id_vars='date', value_vars=categories, 
             var_name='category', value_name='value')

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'title': {'font': 'Lato', 'fontSize': 20, 'anchor': 'start'},
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='Value', axis=alt.Axis(titleAngle=0, titleAlign='left', titleY=-20, titleX=-45, labels=True, ticks=False, labelAlign='left', labelPadding=-5, labelBaseline='middle', tickCount=5, orient='right')),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title="Multiline Chart"
)

st.altair_chart(chart, use_container_width = True)

np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='M')
values = np.random.randn(len(date_range) * 7).cumsum().reshape((len(date_range), 7)) + np.arange(7) * 10
df = pd.DataFrame(values, columns=categories)
df['date'] = date_range

df = df.melt(id_vars='date', value_vars=categories, 
             var_name='category', value_name='value')

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'title': {'font': 'Lato', 'fontSize': 20, 'anchor': 'start'},
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='', axis=alt.Axis(labels=True, ticks=False, labelAlign='left', labelPadding=5, labelBaseline='middle', tickCount=5, orient='right')),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title="Multiline Chart"
).configure_axisRight(
    titleY=-30,
    titleX=30
)

st.write(chart)


# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='M')
values = np.random.randn(len(date_range) * 7).cumsum().reshape((len(date_range), 7)) + np.arange(7) * 10
df = pd.DataFrame(values, columns=categories)
df['date'] = date_range

df = df.melt(id_vars='date', value_vars=categories, 
             var_name='category', value_name='value')

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'title': {'font': 'Lato', 'fontSize': 20, 'anchor': 'start'},
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='Value', axis=alt.Axis(labels=True, ticks=False, labelAlign='left', labelPadding=5, labelBaseline='middle', tickCount=5, orient='right')),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title="Multiline Chart"
).configure_axisRight(
    titleY=-30,
    titleX=30
)

st.altair_chart(chart, use_container_width = True)
st.write(chart)

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='M')
values = np.random.randn(len(date_range) * 7).cumsum().reshape((len(date_range), 7)) + np.arange(7) * 10
df = pd.DataFrame(values, columns=categories)
df['date'] = date_range

df = df.melt(id_vars='date', value_vars=categories, 
             var_name='category', value_name='value')

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'title': {'font': 'Lato', 'fontSize': 20, 'color': '#2c2c2c', 'anchor': 'start', 'subtitleColor': '#5c5c5c', 'subtitleFontSize': 14},
        'background': '#F9F9F9',
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='Value', axis=alt.Axis(labels=True, ticks=False, labelAlign='left', labelPadding=5, labelBaseline='middle', tickCount=5, orient='right')),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title={
        "text": ["Multiline Chart", "Subtitle for the chart"],
        "subtitle": ["Subtitle for the chart"]
    }
)

st.write(chart)

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Simulating data
np.random.seed(42)

categories = ["cat" + str(i) for i in range(1, 8)]
date_range = pd.date_range(start="2020-01-01", end="2020-12-31", freq='M')
values = np.random.randn(len(date_range) * 7).cumsum().reshape((len(date_range), 7)) + np.arange(7) * 10
df = pd.DataFrame(values, columns=categories)
df['date'] = date_range

df = df.melt(id_vars='date', value_vars=categories, 
             var_name='category', value_name='value')

# Colors
colors = ["#000000", "#EC7506", "#0C1433", "#F3A45B", "#7D9CC0", "#444C44", "#746c64"]

# Altair chart with theme
alt.themes.register('custom_theme', lambda: {
    'config': {
        'background': '#fafafa',
        'title': {'font': 'Lato', 'fontSize': 18, 'fontWeight': 'bold', 'color': '#2c2c2c', 'anchor': 'start', 'subtitleColor': '#5c5c5c', 'subtitleFontSize': 12, 'offset': 10},
        'axis': {
            'labelFont': 'Lato',
            'titleFont': 'Lato',
            'grid': True,
            'gridColor': '#ddd',
            'gridWidth': 0.5,
            'domain': False,
        },
        'header': {'labelFont': 'Lato', 'titleFont': 'Lato'},
        'legend': {'labelFont': 'Lato', 'titleFont': 'Lato'},
    }
})
alt.themes.enable('custom_theme')

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('yearmonth(date):T', title='Date', axis=alt.Axis(format='%b %Y')),
    y=alt.Y('value:Q', title='Value', axis=alt.Axis(labels=True, ticks=False, labelAlign='left', labelPadding=15, labelBaseline='middle', tickCount=5, orient='right')),
    color=alt.Color('category:N', scale=alt.Scale(domain=categories, range=colors)),
    tooltip=['date:T', 'value:Q', 'category:N']
).properties(
    width=600,
    height=400,
    title={
        "text": ["Multiline Chart"],
        "subtitle": "Subtitle for the chart",
        "color": "#3a3a3a",
        "subtitleColor": "#5c5c5c",
        "offset": 5,
        "subtitleFontSize": 12,
        "subtitleFont": "Lato"
    }
).configure_view(
    strokeOpacity=0  # Removing the border around the chart for aesthetics
)

st.write(chart)