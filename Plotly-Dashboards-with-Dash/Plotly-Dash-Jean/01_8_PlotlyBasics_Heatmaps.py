import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

# get data for '2010YumaAZ.csv', '2010SantaBarbaraCA.csv', '2010SitkaAK.csv'
df1 = pd.read_csv('Plotly-Dashboards-with-Dash/Data/2010SitkaAK.csv')
df2 = pd.read_csv('Plotly-Dashboards-with-Dash/Data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('Plotly-Dashboards-with-Dash/Data/2010YumaAZ.csv')

# create dictionary for names of each dataframe
df_dict = dict(
    SitkaAK=df1,
    SantaBarbaraCA=df2,
    YumaAZ=df3
)

# create traces for each dataframe in list comprehension
traces = [go.Heatmap(
        x=df_i['DAY'],
        y=df_i['LST_TIME'],
        z=df_i['T_HR_AVG'],
        colorscale='Jet',
        zmin = 5, zmax = 40
    ) for df_i in df_dict.values()
]

# make subplots
fig = tools.make_subplots(rows=1, cols=3,
    subplot_titles=[df_i for df_i in df_dict.keys()],
    shared_yaxes = False,
)

# make a list comprehension to add traces to subplots
[fig.append_trace(trace, 1, i+1) for i, trace in enumerate(traces)]

# update layout
fig['layout'].update(
    title='Hourly Temperatures'
)

# plot
pyo.plot(fig)
