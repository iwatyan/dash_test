import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

# ノードを17個定義
nodes = [{"data": {"id": f"{x}", "label": f"{x}"}} for x in range(17)]

# エッジを定義
edges = [
    {"data": {"source": "0", "target": "1"}},
    {"data": {"source": "0", "target": "2"}},
    {"data": {"source": "0", "target": "3"}},
    {"data": {"source": "0", "target": "4"}},
    {"data": {"source": "2", "target": "3"}},
    {"data": {"source": "3", "target": "4"}},
    {"data": {"source": "4", "target": "5"}},
    {"data": {"source": "5", "target": "1"}},
    {"data": {"source": "1", "target": "6"}},
    {"data": {"source": "2", "target": "7"}},
    {"data": {"source": "2", "target": "8"}},
    {"data": {"source": "3", "target": "9"}},
    {"data": {"source": "4", "target": "10"}},
    {"data": {"source": "4", "target": "11"}},
    {"data": {"source": "4", "target": "12"}},
    {"data": {"source": "5", "target": "13"}},
    {"data": {"source": "5", "target": "14"}},
    {"data": {"source": "6", "target": "15"}},
]
elements = nodes + edges

cyto_compo = cyto.Cytoscape(
    id="dash_cyto_layout",
    style={"width": "400px", "height": "400px"},
    layout={"name": "grid", "rows": 3, "columns": 6},
    elements=elements,
    stylesheet=[
        {"selector": "node", "style": {"content": "data(label)"}},
        # エッジのカーブのスタイルを曲線にする
        {"selector": "edge", "style": {"curve-style": "unbundled-bezier"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
