import callback  # callback.pyのコールバックをインポート
from app import app  # app.pyからappをインポート
from layout import this_layout  # layout.pyから変数this_layout をインポート

app.layout = this_layout

if __name__ == "__main__":
    app.run_server(debug=True)
