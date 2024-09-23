# components/sidebar.py

from dash import html
import dash_bootstrap_components as dbc

def create_sidebar():

    sidebar = html.Div(
        [
            # Header with "YourAppName" text
            html.Div(
                [
                    html.H5("Filter Panel", className="d-flex justify-content-center"),
                    # html.Hr(),
                ],
                className="sidebar-header p-1 mt-1",
            ),
            # Sidebar content container
            html.Div(
                id='sidebar-container',
                className="p-2",
            ),
        ],
        id="sidebar",
        className="sidebar p-2",
    )
    return sidebar
