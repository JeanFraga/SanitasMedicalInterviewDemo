# import Numpy, plotly offline and graphs
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# set random seed for reproducibility to 56
np.random.seed(56)

# create random data
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

# create traces
trace0 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='markers',
                    name='markers')

trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='mylines')

trace2 = go.Scatter(x=x_values,
                    y=y_values-5,
                    mode='lines+markers',
                    name='mylines+markers')

# create data
data = [trace0, trace1, trace2]

# create layout
layout = go.Layout(title='Hello Line Charts!',
                    hovermode='closest')

# create figure
fig = go.Figure(data=data, layout=layout)

# plot figure
pyo.plot(fig, filename='line_chart.html')