# components/dashboard_navbar.py

from dash import html
import dash_bootstrap_components as dbc

def create_dashboard_navbar():

    navbar = dbc.Navbar(
        dbc.Container(
            [
                # Left side: Sidebar toggle and Logo
                dbc.Col(
                    html.Div(
                        [
                            # Sidebar Toggle Button
                            dbc.Button(
                                html.I(className="bi bi-list", style={'font-size': '1.5rem'}),
                                color="link",
                                className="me-3",
                                id="sidebar-toggle",
                                n_clicks=0,  
                                style={'marginTop': '5px'}
                            ),
                            # Logo and title
                            dbc.NavbarBrand(
                                [
                                    html.Img(src="/assets/images/logo.png", height="30px"),
                                    html.Span("YourAppName", className="ms-2"),
                                ],
                                href="/dashboard",
                                className="d-flex align-items-center",
                            ),
                        ],
                        className="d-flex align-items-center",
                        style={'marginLeft': '40px'}
                    ),
                    width="auto",
                ),
                # Center: Page Name (visible only on screens wider than 500px)
                dbc.Col(
                    html.H4("Dashboard", className="text-center m-0 d-none d-sm-block"),
                    className="d-flex justify-content-center align-items-center",
                ),
                # Right side: Home link and "More Apps" dropdown
                dbc.Col(
                    dbc.Nav(
                        [

                            dbc.NavItem(
                                dbc.DropdownMenu(
                                    [
                                        dbc.DropdownMenuItem("Home", href="/", className="custom-dropdown-item"),
                                        html.Hr(),
                                         dbc.DropdownMenuItem("Home", href="/", className="custom-dropdown-item"),
                                        dbc.DropdownMenuItem("Dashboard", href="/dashboard", className="custom-dropdown-item"),
                                        dbc.DropdownMenuItem("Settings", href="/settings", className="custom-dropdown-item"),
                                    ],
                                    nav=True,
                                    in_navbar=True,
                                    label="More Apps",
                                    align_end=True,
                                ),
                                className="position-static"
                            ),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                    width="auto",
                ),
            ],
            fluid=True,
            className="d-flex align-items-center",
        ),
        color="light",
        dark=False,
        sticky="top",
        className="navbar-border-bottom",
    )

    return navbar
