import dash
import dash.dash_table

app = dash.Dash(__name__)

app.layout = dash.dash_table.DataTable(
    # ➊ 引数columnsに列名を渡す
    columns=[
        {"name": "number", "id": "number", "clearable": "first", "deletable": "first", "hideable": "first"},
        {"name": "region", "id": "area", "selectable": "first"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri", "editable": True, "hideable": "last", "renamable": "first", "type": "datetime", "on_change": {"action": "validate", "failure" : "accept"}},
    ],
    # ➋ 引数dataにデータを渡す #pd.to_dictなら'records'形式
    data=[
        {"number": 0, "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    # ➌ テーブルを画面いっぱいに広げない
    fill_width=False,
)

if __name__ == "__main__":
    app.run_server(debug=True)
