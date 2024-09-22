from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

# Import the callbacks registration function
from utils.callbacks import register_callbacks

# Initialize the Dash app
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder='assets'
)

# Expose server for deployment
server = app.server

# Register callbacks
register_callbacks(app)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dash.page_container  # Container for rendering pages
])

if __name__ == '__main__':
    app.run_server(debug=True)
