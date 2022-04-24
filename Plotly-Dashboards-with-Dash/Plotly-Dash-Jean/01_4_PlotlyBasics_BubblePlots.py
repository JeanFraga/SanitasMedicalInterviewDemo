# import plotly offline, plotly graph objects, and pandas
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# import 'mpg.csv' into a DataFrame:
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/mpg.csv')
print(df.columns)
# sort the DataFrame by the 'horsepower' column:
# df = df.sort_values(by='horsepower', ascending=True)
df = df[df['horsepower'].apply(lambda x:x.isnumeric())]
df['horsepower'] = df['horsepower'].astype('int64')

# create traces using a list comprehension:
data = [
    go.Scatter(
        x=df['horsepower'],
        y=df['mpg'],
        text=df['name'],
        mode='markers',
        marker={
                'size': df['weight']/100,
                # 'size': df['cylinders']*3,
                # 'opacity': 0.5,
                # 'line': {'width': 0.5, 'color': 'white'}
                'color': df['cylinders'],
                'showscale': True,
                }
    )
]

# create a layout
layout = go.Layout(
    title='Bubble Chart from mpg.csv',
    hovermode='closest',
    xaxis={'title': 'Horsepower'},
    yaxis={'title': 'Miles Per Gallon'},
    # showlegend=False
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)