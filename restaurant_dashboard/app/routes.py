# routes.py
from flask import Flask, render_template
import json, plotly
from plots import generate_plots

app = Flask(__name__)

@app.route('/')
def index():
    figures = generate_plots()
    ids = ['figure-{}'.format(i) for i,_ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
			    ids = ids,
			    figuresJSON = figuresJSON)

@app.route('/employees')
def employees():
    return render_template('employees.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

if __name__ == '__main__':
    app.run(debug = True)
