import dash
import plotly.express as px
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = dcc.Graph(
    # figure属性にbar関数で作成したfigureを渡す
    figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])
)

if __name__ == "__main__":
    app.run_server(debug=True)
