import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

elements = [
    # ❶ 親ノードの定義
    {"data": {"id": "p_A", "label": "Parent A"}},
    {"data": {"id": "p_B", "label": "Parent B"}},
    # ❷ 子ノードの定義
    {"data": {"id": "c_a", "label": "child a", "parent": "p_A"}},  # ❹
    {"data": {"id": "c_b", "label": "child b", "parent": "p_B"}},  # ❹
    {"data": {"id": "c_c", "label": "child c", "parent": "p_A"}},  # ❹
    {"data": {"id": "c_d", "label": "child d"}},  # ❺ 親なし
    # ❸ エッジの定義
    {"data": {"source": "p_A", "target": "p_B"}, "classes": "parents"},  # 親ノード同士
    {"data": {"source": "c_a", "target": "c_b"}, "classes": "children"},  # 子ノード同士
    {"data": {"source": "c_a", "target": "c_c"}, "classes": "children"},  # 子ノード同士
    {"data": {"source": "p_A", "target": "c_d"}, "classes": "parents children"}  # 親と子ノード同士
]

cyto_compo = cyto.Cytoscape(
    id="dash_cyto_compound-node",
    layout={"name": "circle"},
    style={"width": "350px", "height": "450px"},
    elements=elements,
    stylesheet=[
        {"selector": "node", "style": {"content": "data(label)"}},
        {"selector": ".parents", "style": {"line-color": "red"}},
        {"selector": ".children", "style": {"line-style": "dashed"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
