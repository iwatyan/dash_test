import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.P("こんにちは。昨日は雪が降りました。")

if __name__ == "__main__":
    app.run_server(debug=True)
