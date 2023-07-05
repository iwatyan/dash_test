import dash
from dash import dcc

app = dash.Dash(__name__)
app.layout = dcc.Dropdown()
app.run_server(debug=True)
