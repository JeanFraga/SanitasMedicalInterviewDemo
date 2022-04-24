# import pandas, numpy and plotly offline and graphs
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# get data from 'nst-est2017-alldata.csv'
df = pd.read_csv('Plotly-Dashboards-with-Dash/SourceData/nst-est2017-alldata.csv')

# create df2 that keep 'DIVISION' column where it is equal to '1'
df2 = df[df['DIVISION'] == '1']
# set index to 'NAME' column
df2 = df2.set_index('NAME')
# create list comprehension that keep columns that start with 'POP'
cols = [col for col in df2.columns if col.startswith('POP')]
# filter df2 to keep only columns that start with 'POP'
df2 = df2[cols]

# data for plot in a list comprehension that uses columns and name
data = [go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index]

# plot the data
pyo.plot(data, filename='Plotly-Dashboards-with-Dash/01_2_PlotlyBasics_LineCharts2.html')