import dash
from dash_canvas import DashCanvas
from dash_canvas.utils import array_to_data_url
from skimage import io

# ➊ 画像を変数に渡す
data = array_to_data_url(io.imread("plotly-dash-book-master/ch09_dash_additional_components/img/bird1.png"))
# imreadでnumpy.ndarrayに変換後、array_to_data_urlで文字列に変換
app = dash.Dash(__name__)

app.layout = DashCanvas(
    id="first-image",
    image_content=data,  # ➋ コンポーネントへの画像の読み込み
    width=800,  # ➌ キャンバスの横幅
    lineWidth=12,  # ➌書き込みの線の太さ
    goButtonTitle="nothing",  # ➌ saveボタンのタイトル変更
    lineColor="lime",  # ➍ 書き込み線の色
    hide_buttons=["zoom", "pan", "line", "select"],  # ➍ 編集ツールの設定
)

if __name__ == "__main__":
    app.run_server(debug=True)
