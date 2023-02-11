from flask import Flask, render_template, url_for, send_file, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from analysis import Analysis
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    resp = Response(render_template('plot.html'))
    return resp

@app.route('/plot.png/<is_null>')
def plot_png(is_null):
    fig = Analysis.sample_plot(is_null)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    resp = Response(output.getvalue(), mimetype='image/png')
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

if __name__ == "__main__":
    app.run(debug=True)
