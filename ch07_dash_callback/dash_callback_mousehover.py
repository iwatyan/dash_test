import json

import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output

# ➊ データの作成（gapminderデータの2007年分のみ）
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# ➋ アプリケーションのレイアウト
app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        # ➍ 散布図の作成
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
            ),
        ),
        # ➎ ホバーデータを表示するPコンポーネント
        html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)

# ➌ コールバック
@app.callback(
    Output("hoverdata-p", "children"), Input("gapminder-g", "clickData")  # ➏
)  # ➐
def show_hover_data(clickData):  # ➑
    return json.dumps(clickData)  # ➒


if __name__ == "__main__":
    app.run_server(debug=True)
