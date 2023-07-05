import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import ALLSMALLER, MATCH, Input, Output, State

# gapminderデータを読み込む
gapminder = px.data.gapminder()

app = dash.Dash(__name__)

# ➊ レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop"),
        html.Div(id="show_drop", children=[]),  # ドロップダウンと選択された値が追加されるUI
    ],
    style={"width": "80%", "margin": "2% auto"},
)

# ➋ コールバック1
@app.callback(
    Output("show_drop", "children"),
    Input("add_drop", "n_clicks"),
    State("show_drop", "children"),
    prevent_initial_call=True,# 最初の呼び出しをしたら、n_clicksが0であり、エラーを引き起こす
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            ),  # ➌ 文字列を表示するコンポーネント
            html.P(id={"type": "text_show", "index": n_clicks}),
        ]
    )

    children.append(new_layout)
    return children


# コールバック2
@app.callback(
    Output({"type": "text_show", "index": MATCH}, "children"),
    # ➊ IDキー"index"に渡すセレクタをALLSMALLERに更新
    Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
)
def update_graph(selected_values):
    return str(selected_values)


app.run_server(debug=True)
