# components/dashboard_navbar.py

from dash import html
import dash_bootstrap_components as dbc

def create_dashboard_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                # Left side: Sidebar toggle and Logo
                html.Div(
                    [
                        # Sidebar Toggle Button
                        dbc.Button(
                            html.I(className="bi bi-list", style={'font-size': '1.5rem','paddingTop': '20px'}),
                            color="link",
                            className="me-3",
                            id="sidebar-toggle",
                            n_clicks=0,  
                        ),
                        # Logo and title
                        dbc.NavbarBrand(
                            [
                                html.Img(src="/assets/images/logo.png", height="30px"),
                                html.Span("YourAppName", className="ms-2"),
                            ],
                            href="/dashboard",
                            className="d-flex align-items-center",
                            style={'marginLeft': '50px'},
                        ),
                    ],
                    className="d-flex align-items-center",
                ),
                # Right side: Home link and "More Apps" dropdown
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink("Home", href="/", className="me-2")
                        ),
                        dbc.NavItem(
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("App 1", href="#"),
                                    dbc.DropdownMenuItem("App 2", href="#"),
                                    dbc.DropdownMenuItem("App 3", href="#"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="More Apps",
                                align_end=True,
                                toggle_style={"marginRight": "15px"},
                            ),
                            className="position-static"
                        ),
                    ],
                    className="ms-auto",
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="light",
        dark=False,
        sticky="top",
        className="navbar-border-bottom",
    )
    return navbar
