# components/navbar.py

from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.Navbar(
        [
            dbc.Container(
                [
                    # Left side: Icon and Title
                    dbc.NavbarBrand(
                        [
                            html.Img(src="/assets/images/logo.png", height="40px"),
                            html.Span("YourAppName", className="ms-2"),
                        ],
                        href="/",
                        className="d-flex align-items-center",
                    ),
                    # Right side: Login and Get Started buttons
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink("Login", href="/login", className="me-2")
                            ),
                            dbc.Button(
                                "Get Started", color="primary", href="/signup"
                            ),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                ],
                fluid=True,
            )
        ],
        color="white",
        dark=False,
        sticky="top",
        className="navbar-border-bottom"
    )
    return navbar
