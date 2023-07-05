import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([html.Div(className="circle")])  # className属性を設定

if __name__ == "__main__":
    app.run_server(debug=True)
