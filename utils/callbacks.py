# utils/callbacks.py

from dash import Output, Input, State, callback, html
from utils.helpers import create_dashboard_sidebar_filters 

# Register callback function 
def register_callbacks(app):
    @app.callback(
        [Output("sidebar", "className"), Output("page-content", "className")],
        [Input("sidebar-toggle", "n_clicks")],
        [State("sidebar", "className"), State("page-content", "className")],
    )
    def toggle_sidebar(n_clicks, sidebar_class, content_class):
        if n_clicks:
            if "closed" in sidebar_class:
                # Remove 'closed' from sidebar and 'full-width' from content
                new_sidebar_class = sidebar_class.replace(" closed", "")
                new_content_class = content_class.replace(" full-width", "")
            else:
                # Add 'closed' to sidebar and 'full-width' to content
                new_sidebar_class = sidebar_class + " closed"
                new_content_class = content_class + " full-width"
            return new_sidebar_class, new_content_class
        return sidebar_class, content_class


    # Side bar filter panels for each page
    @app.callback(
        Output('sidebar-container', 'children'),
        Input('url', 'pathname')
    )
    def update_sidebar(pathname):
        if pathname == '/dashboard':
            return create_dashboard_sidebar_filters()
        # elif pathname == '/app2':
        #     return create_app2_sidebar()
        # # ... other pages ...
        else:
            return html.Div("No sidebar content")

