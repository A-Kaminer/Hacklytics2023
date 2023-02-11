from flask import Flask, render_template, url_for, send_file, Response
from analysis import Analysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    filename = Analysis.make_random_plot()
    resp = Response(render_template('plot.html', img_name=filename))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

if __name__ == "__main__":
    app.run(debug=True)
