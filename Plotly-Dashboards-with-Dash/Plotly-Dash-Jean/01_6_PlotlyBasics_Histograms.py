import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/mpg.csv')

# drop rows with '?' in the 'mpg' column
df = df[df['mpg'] != '?']
# conver mpg to numeric
df['mpg'] = df['mpg'].astype('float')

# create data variable
data = [
    go.Histogram(
        x=df['mpg'],
        # nbinsx=20,
        xbins=dict(
            start=0,
            end=50,
            # size=20
        )
    )
]

# create layout variable
layout = go.Layout(
    title='Histogram of MPG',
    xaxis=dict(
        title='Miles Per Gallon',
        titlefont=dict(
            size=30,
            color='rgb(200, 107, 107)'
        ),
        tickfont=dict(
            size=20,
            color='rgb(107, 200, 107)'
        )
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=30,
            color='rgb(200, 107, 107)'
        ),
        tickfont=dict(
            size=20,
            color='rgb(107, 200, 107)'
        )
    )
)

# create fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
