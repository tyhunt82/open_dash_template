# components/footer.py

from dash import html
import dash_bootstrap_components as dbc

def create_footer():
    footer = html.Footer(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.P(
                                "© 2023 YourAppName. All rights reserved.",
                                className="text-center mb-0"
                            ),
                            width=12,
                        )
                    ]
                )
            ],
            fluid=True,
            className="py-3",
        ),
        className="footer bg-light mt-auto",
    )
    return footer
