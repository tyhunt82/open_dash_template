# components/hero.py

from dash import html
import dash_bootstrap_components as dbc

def create_hero():
    IMAGES_STYLE = {"minHeight": "175px","maxHeight": "300px"}

    hero = html.Div(
        [
            dbc.Container(
                [
                    html.H1("Welcome to YourAppName", className="display-3 text-center"),
                    html.P(
                        "YourAppName is a platform that allows you to do amazing things. "
                        "Experience the simplicity and efficiency in managing your tasks.",
                        className="lead text-center",
                    ),
                    html.Hr(className="my-4"),
                    # Placeholder for images or carousel
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src="/assets/images/placeholder1.jpg",
                                    className="img-fluid",
                                    style=IMAGES_STYLE,
                                ),
                                className="d-flex justify-content-center p-3",
                                md=4,
                            ),
                            dbc.Col(
                                html.Img(
                                    src="/assets/images/placeholder2.jpg",
                                    className="img-fluid",
                                    style=IMAGES_STYLE,
                                ),
                                className="d-flex justify-content-center p-3",
                                md=4,
                            ),
                            dbc.Col(
                                html.Img(
                                    src="/assets/images/placeholder3.jpg",
                                    className="img-fluid",
                                    style=IMAGES_STYLE,
                                ),
                                 className="d-flex justify-content-center p-3",
                                md=4,
                            ),
                        ],
                        className="mt-4",
                    ),
                ],
                className="py-5",
                # fluid=True, 
                style={'paddingLeft': '20px'}
            )
        ],
        className="bg-light hero-section",
        style={'flex': '1','paddingTop': '20px','paddingBottom': '20px'} 
        
    )
    return hero
