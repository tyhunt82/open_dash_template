# app.py

from dash import Dash, html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc
from utils.helpers import create_dashboard_sidebar_filters 

# Import the callbacks registration function
from utils.callbacks import register_callbacks

# Initialize the Dash app
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css'
    ],
    assets_folder='assets'
)

# Expose server for deployment
server = app.server

# Register callbacks
register_callbacks(app)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dash.page_container 
])


if __name__ == '__main__':
    app.run_server(debug=True)
