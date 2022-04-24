from matplotlib.axis import XAxis
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_X = np.random.randint(1,101,100)
random_Y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_X,
                    y=random_Y,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,153)',
                        symbol='pentagon',
                        line=dict(width=2)
                    ))]

layout = go.Layout(title='Hello Plotly!',
                    xaxis=dict(title='My X-Axis'),
                    yaxis=dict(title='My Y-Axis'),
                    hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='scatter_3.html')