import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

# Load data from CSV file
df = pd.read_csv('data.csv')

# Define the chart type and data
data = [go.Scatter(x=df['x'], y=df['y'], mode='markers')]

# Define the layout
layout = go.Layout(title='Interactive Data Visualization Tool', xaxis_title='X Axis', yaxis_title='Y Axis')

# Create the figure object
fig = go.Figure(data=data, layout=layout)

# Render the chart
pyo.plot(fig, filename='interactive_data_visualization.html')
