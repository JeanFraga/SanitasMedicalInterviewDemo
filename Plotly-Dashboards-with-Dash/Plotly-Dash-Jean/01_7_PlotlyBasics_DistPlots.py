from matplotlib.pyplot import hist
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

# x = np.random.randn(1000)
# create x1, x2, x3 and x4 with 200 random values each and -2 to +4
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

# create a dataframe with the 4 columns
df = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4})

# create hist_data with the 4 columns in a list comprehension
hist_data = [df[column] for column in df.columns]

# create group_labels with the 4 columns in a list comprehension
group_labels = [column for column in df.columns]

# hist_data = [x]
# group_labels = ['distplot']


fig = ff.create_distplot(
    hist_data,
    group_labels,
    bin_size=[.2,.1,.3,.4],
    # show_rug=True,
    # show_curve=False
)
pyo.plot(fig)
