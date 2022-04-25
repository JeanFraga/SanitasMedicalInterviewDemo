import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('Hello Dash!'),
        html.Div('Dash: A web application framework for Python.'),
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
                ),
            )
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
