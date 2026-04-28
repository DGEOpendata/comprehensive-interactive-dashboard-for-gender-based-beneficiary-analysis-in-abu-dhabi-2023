python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template, jsonify

# Load the dataset
data = pd.read_csv('2023_Beneficiaries_Distribution_FullYear.csv')

# Pre-process the data
data['Quarter'] = data['Quarter'].astype(str)

# Create a Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart_data')
def chart_data():
    # Example: Filter data for a specific type
    data_filtered = data.groupby(['Quarter', 'Gender'])['Count'].sum().reset_index()
    return jsonify(data_filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
