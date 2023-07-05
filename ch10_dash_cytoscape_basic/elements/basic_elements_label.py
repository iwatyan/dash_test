import dash
import dash_cytoscape as cyto
from dash import html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# ネットワークの構成要素の定義
elements = [
    # ❶ ノードの定義（データ辞書内でラベル文字列を指定）
    {"group": "nodes", "data": {"id": "A", "label": "Alice"}, "position": {"x": 0, "y": -100}, "selected": True, "locked": True},
    {"group": "nodes", "data": {"id": "B", "label": "Bob"}, "position": {"x": -100, "y": 0}, "selectable": False},
    {"group": "nodes", "data": {"id": "C", "label": "Carol"}, "position": {"x": 100, "y": 0}, "locked": True},
    {"group": "nodes", "data": {"id": "D", "label": "David"}, "position": {"x": 100, "y": 100}, "grabbable": False},
    # エッジの定義
    {"group": "edges", "data": {"source": "A", "target": "B"}},
    {"group": "edges", "data": {"source": "A", "target": "C"}},
    {"group": "edges", "data": {"source": "C", "target": "D"}},
]

# Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="basic_elements",
    style={"width": "600px", "height": "600px", "padding": "50px"},
    # ネットワークの構成要素の定義
    elements=elements,
    # ノード配置方法の定義
    layout={"name": "preset"},
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
