import dash
import dash.dash_table
import pandas as pd
from dash import html

df = pd.read_csv("plotly-dash-book-master/ch08_dash_standard_components/data/kitakyushu_hinanjo.csv", encoding="shift-jis")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash.dash_table.DataTable(
            page_size=700,  # ➊ 1ページの表示行数
            virtualization=True,  # ➋ 仮想化
            style_cell={
                "textAlign": "center",  # テキストを中央寄せ
                "maxWidth": "80px",  # ➋ 最大横幅
                "minWidth": "80px",  # ➌ 最小横幅
                "whiteSpace": "normal",  # ➍ 文字を折り返し表示
            },
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
        )
    ]
)
# 仮想化することで、ページの表示速度が改善するが、この際には以下の点に注意する必要がある
# 1. 列の横幅を固定する
# 2. 行の高さを同じにする
# 3. 追加のスタイル更新を競ってしても、初期設定の横幅と高さには影響しない

app.run_server(debug=True)
