#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
# import plotly offline, plotly graph objects, and pandas
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
# import 'mpg.csv' into a DataFrame turn '?' into NaN:
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/mpg.csv', na_values='?')
print(df.columns)

# drop the rows with missing values:
df = df.dropna()
# turn 'horsepower' into a numeric value:
# df['horsepower'] = df['horsepower'].astype('int64')

# df = df[df['horsepower'].apply(lambda x:x.isnumeric())]
# df['horsepower'] = df['horsepower'].astype('int64')

# create data by choosing fields for x, y and marker size attributes
data = [
    go.Scatter(
        x=df['weight'],
        y=df['acceleration'],
        text=df['name'],
        mode='markers',
        marker=dict(
            size=df['mpg'],
            color=df['model_year'],
            showscale=True,
        )
    )
]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Bubble Chart from mpg.csv',
    hovermode='closest',
    xaxis={'title': 'Weight'},
    yaxis={'title': 'Acceleration'},
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
