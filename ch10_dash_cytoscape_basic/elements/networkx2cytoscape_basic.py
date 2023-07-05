import dash
import dash_cytoscape as cyto
import networkx as nx
import pandas as pd
from dash import html

app = dash.Dash(__name__)

# 隣接行列が定義されたCSVファイルを読み込み
df = pd.read_csv("plotly-dash-book-master/ch10_dash_cytoscape_basic/elements/data/adj_matrix.csv", index_col=0)

# Step 1. pandasのデータフレーム ⇨ NetworkXのGraphオブジェクト
G = nx.from_pandas_adjacency(df)

# Step 2. NetworkXのGraphオブジェクト ⇨ Cytoscape用のデータ形式
cy_data = nx.readwrite.json_graph.cytoscape_data(G)

# Step 3. Cytoscapeのデータ形式 ⇨ Dash Cytoscapeのデータ形式
dash_cy_elements = cy_data["elements"]["nodes"] + cy_data["elements"]["edges"]

cyto_compo = cyto.Cytoscape(
    id="networkx2cytoscape",
    style={"width": "400px", "height": "400px"},
    layout={"name": "breadthfirst", "roots": "#A"},
    elements=dash_cy_elements,  # ❶ 変換後のデータを指定
    stylesheet=[{"selector": "node", "style": {"content": "data(id)"}}],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
