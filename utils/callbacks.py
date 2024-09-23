# utils/callbacks.py

from dash import Output, Input, State, callback

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
