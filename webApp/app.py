from flask import Flask, render_template, url_for, send_file, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from analysis import Analysis
import io

app = Flask(__name__)

analysis = Analysis()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    resp = Response(render_template('plot.html'))
    return resp

@app.route('/about')
def about():
    
    andrew_github="https://github.com/A-Kaminer"


    about_andrew = get_file_text("bios/about_andrew.txt")
    about_eddie = get_file_text("bios/about_eddie.txt")
    about_daniel = get_file_text("bios/about_daniel.txt")
    about_rohan = get_file_text("bios/about_rohan.txt")

    return render_template('about.html', about_andrew=about_andrew, 
            about_eddie=about_eddie, about_daniel=about_daniel, 
            about_rohan=about_rohan, andrew_github=andrew_github)

@app.route('/plot.png/<is_null>')
def plot_png(is_null):
    fig = analysis.sample_plot(is_null)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    resp = Response(output.getvalue(), mimetype='image/png')
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

def get_file_text(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    app.run(debug=True)
