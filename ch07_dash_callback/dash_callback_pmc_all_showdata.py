import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import ALL, Input, Output, State

# gapminderデータを読み込む
gapminder = px.data.gapminder()

app = dash.Dash(__name__)

# ➊ レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop"),  # 新たなドロップダウンを追加するボタン（➋）
        html.Div(id="show_drop", children=[]),  # ドロップダウンを追加するDiv（➌）
        html.P(id="my_text"),  # テキストを描画するP（➍）
    ],
    style={"width": "80%", "margin": "2% auto"},
)

# ➎ コールバック1
@app.callback(
    Output("show_drop", "children"),
    Input("add_drop", "n_clicks"),
    State("show_drop", "children"),
    prevent_initial_call=True,  # ➏ 最初の呼び出しをしたら、n_clicksが0であり、エラーを引き起こす
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},  # ➐ idがmy_dropdownのコンポーネントの中で、indexがn_clicksであるコンポーネントのみをセレクタが抽出している。*n_clicksはクリックされるたびに1増えるから一意性を持つ
                # セレクタにより同一IDを持つコンポーネントについて、抽出するコンポーネントの条件を追加することができる
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            )
        ]
    )
    children.append(new_layout)  # ➑
    return children


# ➒ コールバック2
@app.callback(
    Output("my_text", "children"),
    Input({"type": "my_dropdown", "index": ALL}, "value"),  # ➓
    prevent_initial_call=True,
)
def update_graph(selected_values):
    # 全てのドロップダウンで選択された国のリストを文字列にする
    # リストの'[]'ごと文字列にしてる
    return str(selected_values)


app.run_server(debug=True)
