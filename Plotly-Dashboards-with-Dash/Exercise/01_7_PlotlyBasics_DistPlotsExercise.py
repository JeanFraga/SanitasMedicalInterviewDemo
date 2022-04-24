#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('Plotly-Dashboards-with-Dash/Data/iris.csv')

# create traces:
traces = [
    df[df['class'] == i]['petal_length']
    for i in df['class'].unique()
]

# create a list of labels:
group_labels = [
    i for i in df['class'].unique()
]

# Create a figure from data and layout:
fig = ff.create_distplot(
    traces,
    group_labels,
    bin_size=[.2,.1,.3,.4],
    show_rug=True,
    # show_curve=False
)

# Plot the fig:
pyo.plot(fig)
