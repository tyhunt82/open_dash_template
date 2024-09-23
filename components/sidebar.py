# components/sidebar.py

from dash import html
import dash_bootstrap_components as dbc

def create_sidebar():

    sidebar = html.Div(
        [
            # Header with "YourAppName" text
            html.Div(
                [
                    html.H4("YourAppName", className="d-flex justify-content-center"),
                    html.Hr(),
                ],
                className="sidebar-header p-2 mt-2",
            ),
            # Sidebar content (can be navigation links or other content)
            html.Div(
                [
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.Button("🏠 Home", href="/", color="primary", outline=True, className="w-100 mb-2", style={'textAlign': 'left', 'paddingLeft': '10px'})),
                            dbc.NavItem(dbc.Button("📱 App #1", href="#", color="primary", outline=True, className="w-100 mb-2", style={'textAlign': 'left', 'paddingLeft': '10px'})),
                            dbc.NavItem(dbc.Button("🌏 App #2", href="#", color="primary", outline=True, className="w-100 mb-2", style={'textAlign': 'left', 'paddingLeft': '10px'})),
                            dbc.NavItem(dbc.Button("⚙️ Settings", href="#", color="primary", outline=True, className="w-100 mb-2", style={'textAlign': 'left', 'paddingLeft': '10px'})),
                        ],
                        vertical=True,
                    ),
                ],
                className="p-1",
            ),

        ],
        id="sidebar",
        className="sidebar p-2",  # Added p-2 class for padding
    )
    return sidebar
