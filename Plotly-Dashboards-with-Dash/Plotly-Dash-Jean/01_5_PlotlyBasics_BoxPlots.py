# import plotly offline mode and graph objects
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
# y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

# create a box plot
data = [
    go.Box(
        # y=y,
        y=snodgrass,
        boxpoints='all', # display the original data points
        name='QCS',
        # boxpoints='all', # display the original data points
        # jitter=0.3,      # spread them out so they all appear
        # pointpos=-1.8,    # offset them to the left of the box
    ),
    go.Box(
        y=twain,
        boxpoints='all', # display the original data points
        name='Twain',
    )
]
# add a layout
layout = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

# plot the box plot
pyo.plot(fig)