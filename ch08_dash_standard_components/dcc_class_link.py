import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Link("/test", href="/test"),  # ➊
        html.Br(),
        dcc.Link("/test2", href="/test2"),
        html.Br(),
        dcc.Link("/test3", href="/test3"),
        html.Br(),
        dcc.Link("home", href="/"),
        html.Br(),
        html.A("dash", href="https://dash.plotly.com")
    ],
    style={"fontSize": 30, "textAlign": "center"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
