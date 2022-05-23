from dash import Dash, html, dcc, dependencies
import plotly.graph_objs as go
import pandas as pd

app = Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True)
