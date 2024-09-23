# pages/dashboard.py

from dash import html, dcc
import dash
import dash_bootstrap_components as dbc

from components.dashboard_navbar import create_dashboard_navbar
from components.sidebar import create_sidebar
from components.footer import create_footer

dash.register_page(__name__, path='/dashboard', name='Dashboard')

# pages/dashboard.py

layout = html.Div(
    [
        create_dashboard_navbar(),
        html.Div(
            [
                create_sidebar(),
                html.Div(
                    id="page-content",
                    className="content",  # Ensure this className is set
                    children=[
                        # Main content goes here
                        html.H2("Dashboard Content"),
                        html.P("This is where your dashboard content will appear."),
                    ],
                    style={'padding': '20px', 'flex': '1'},
                ),
            ],
            className="d-flex",
            style={'flex': '1'},
        ),
    ],
    style={'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh'}
)
