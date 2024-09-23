# pages/home.py

from dash import html
import dash
import dash_bootstrap_components as dbc

from components.navbar import create_navbar
from components.hero import create_hero
from components.footer import create_footer

dash.register_page(__name__, path='/', name='Home')

layout = html.Div(
    [
        create_navbar(),
        html.Div(
            create_hero(),
            style={'flex': '1', 'padding': '20px'}
        ),
        create_footer(),
    ],
    style={'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh'}
)