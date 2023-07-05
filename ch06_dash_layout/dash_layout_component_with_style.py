import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    # ➊ スタイルの設定
    style={
        "fontSize": 50,  # 文字サイズ
        "color": "white",  # 文字色
        "backgroundColor": "#000000",  # 背景色
    },
)

if __name__ == "__main__":
    app.run_server(debug=True)
