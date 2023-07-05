import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import MATCH, Input, Output, State

# gapminderデータを読み込む
gapminder = px.data.gapminder()
# 横に2つのコンポーネントを並べるためのスタイル
half_style = {"width": "50%", "display": "inline-block"}

app = dash.Dash(__name__)

# 2つのコンポーネントを持つレイアウト
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop", n_clicks=0),
        html.Div(id="my_div", children=[]),
    ]
)

# ➊ コールバック1
@app.callback(
    Output("my_div", "children"),
    Input("add_drop", "n_clicks"),
    State("my_div", "children"),
    prevent_initial_call=True,# 最初の呼び出しをしたら、n_clicksが0であり、エラーを引き起こす
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            ),
            dcc.Dropdown(
                id={"type": "my_dropdown2", "index": n_clicks},
                options=[
                    {"label": col, "value": col} for col in gapminder.columns[3:6]
                ],
                value="lifeExp",
            ),
            dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
        ],
        style=half_style,
    )  # 横に2つのレイアウトを並べるためstyleを渡す
    children.append(new_layout)
    return children


# ➋コールバック2
@app.callback(
    # ➌ indexにMATCHを渡す
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),
    Input({"type": "my_dropdown2", "index": MATCH}, "value"),
)
def update_graph(selected_value, selected_col):
    gap = gapminder[gapminder["country"] == selected_value]
    return px.line(gap, x="year", y=selected_col)


app.run_server(debug=True)
