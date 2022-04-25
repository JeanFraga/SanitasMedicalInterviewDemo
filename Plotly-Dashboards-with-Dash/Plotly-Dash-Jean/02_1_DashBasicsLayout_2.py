import dash
from dash import dcc
from dash import html

app = dash.Dash()

colors = dict(
    background = '#111111',
    text = '#7FDBFF',
)

app.layout = html.Div(
    children=[
        html.H1('Hello Dash!', style=dict(
            textAlign='center',
            color=colors['text'],
        )),
        dcc.Graph(
            id='example-graph',
            figure=dict(
                data=[
                    dict(
                        x=[1, 2, 3],
                        y=[4, 1, 2],
                        type='bar',
                        name='SF'
                    ),
                    dict(
                        x=[1, 2, 3],
                        y=[2, 4, 5],
                        type='bar',
                        name='Montreal'
                    ),
                ],
                layout=dict(
                    title='Bar Plots!',
                    xaxis=dict(title='City'),
                    yaxis=dict(title='Number of people'),
                    plot_bgcolor=colors['background'],
                    paper_bgcolor=colors['background'],
                    font=dict(color=colors['text']),
                ),
            ),
        ),
    ],
    style=dict(
        backgroundColor=colors['background'],
    ),
)

if __name__ == '__main__':
    app.run_server(debug=True)
