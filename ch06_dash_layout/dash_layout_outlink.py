import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [html.H1("スタイル"), dcc.Input(placeholder="スタイルシートテスト"), dcc.Graph()]
)

if __name__ == "__main__":
    app.run_server(debug=True)
