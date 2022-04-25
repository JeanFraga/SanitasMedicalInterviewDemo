#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/abalone.csv')

# create a data variable:
data = [
    go.Histogram(
        x=df['length'],
        xbins=dict(
            start=0,
            end=1,
            size=0.02
        )
    )
]

# add a layout
layout = go.Layout(
    title = 'Histogram of Abalone Length',
    xaxis = dict(
        title = 'Length',
        titlefont = dict(
            size = 50,
            color = 'rgb(200, 107, 107)'
        ),
        tickfont = dict(
            size = 20,
            color = 'rgb(107, 200, 107)'
        )
    ),
    yaxis = dict(
        title = 'Count',
        titlefont = dict(
            size = 50,
            color = 'rgb(200, 107, 107)'
        ),
        tickfont = dict(
            size = 20,
            color = 'rgb(107, 200, 107)'
        )
    )
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)