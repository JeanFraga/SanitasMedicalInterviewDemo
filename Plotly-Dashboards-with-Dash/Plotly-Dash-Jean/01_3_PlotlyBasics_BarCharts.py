# import numpy, pandas, and plotly graphs and offline mode
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# read from Plotly-Dashboards-with-Dash/Data/2018WinterOlympics.csv
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/2018WinterOlympics.csv')
print(df.head())

# create traces1
trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker=dict(color='#FFD700'))

# create traces2 for silver medals
trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker=dict(color='#9EA0A1'))

# create traces3 for bronze medals
trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker=dict(color='#CD7F32'))

# create data
# data = [go.Bar(
#     x=df['NOC'],
#     y=df['Total'],
# )]

# create data with traces1, traces2, and traces3
data = [trace1, trace2, trace3]


# create layout for Nested Plot
# layout = go.Layout(title='Medals by Country')

# create layout for stacked bar chart
layout = go.Layout(title='Medals by Country',
                    barmode='stack',
                    # hovermode='closest'
                    )

# create figure
fig = go.Figure(data=data, layout=layout)

# create plot
pyo.plot(fig)