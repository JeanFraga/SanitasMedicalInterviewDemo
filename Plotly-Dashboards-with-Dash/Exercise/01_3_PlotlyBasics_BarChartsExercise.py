#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/mocksurvey.csv', index_col=0)
print(df.head())

# create traces using a list comprehension:
# dat stacked vertically
#  data = [
#     go.Bar(x=df.index,
#                y=df[col],
#                name=col) for col in df.columns
#         ]

# create the traces for the horizontal bar chart:
data = [
    go.Bar(
        x=df[col],
        y=df.index,
        orientation='h',
        name=col
    ) for col in df.columns
]       

# create a layout, remember to set the barmode here
# layout = go.Layout(title='Mock Survey',
#                    barmode='stack')

# create layout for stacked bar chart
layout = go.Layout(title='Mock Survey',
                    barmode='stack',
                    hovermode='y')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
