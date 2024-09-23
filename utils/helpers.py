# helpers.py

from dash import Dash, html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc



def create_dashboard_sidebar_filters():
    LABEL_STYLE = {"font-size": "0.8rem",
                  "white-space": "nowrap",
                  "overflow": "hidden",
                  "text-overflow": "ellipsis",
                  "display": "block",
                  "margin-bottom": "0px"}
    return html.Div([
       
        # Dropdown filter
        html.Label("Select Category", style=LABEL_STYLE),
        dcc.Dropdown(
            id='category-dropdown',
            options=[
                {'label': 'Category A', 'value': 'A'},
                {'label': 'Category B', 'value': 'B'},
                {'label': 'Category C', 'value': 'C'},
            ],
            value='A',
            className="mb-3"
        ),
        
        # Date Range Picker
        html.Label("Date Range", style=LABEL_STYLE),
        dcc.DatePickerRange(
            id='date-range-picker',
            start_date_placeholder_text="Start Date",
            end_date_placeholder_text="End Date",
            className="mb-3"
        ),
        
        # Slider
        html.Label("Value Range", style=LABEL_STYLE),
        dcc.RangeSlider(
            id='value-range-slider',
            min=0,
            max=100,
            step=5,
            marks={0: '0', 25: '25', 50: '50', 75: '75', 100: '100'},
            value=[25, 75],
            className="mb-3"
        ),
        
        # Radio Items
        html.Label("Select Option", style=LABEL_STYLE),
        dbc.RadioItems(
            id='option-radio',
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
            ],
            value=1,
            className="mb-3"
        ),
        
        # NEW: Multi-Select Dropdown
        html.Label("Select Multiple Items", style=LABEL_STYLE),
        dcc.Dropdown(
            id='multi-select-dropdown',
            options=[
                {'label': 'Item 1', 'value': 'item1'},
                {'label': 'Item 2', 'value': 'item2'},
                {'label': 'Item 3', 'value': 'item3'},
                {'label': 'Item 4', 'value': 'item4'},
            ],
            multi=True,
            value=['item1'],
            className="mb-3"
        ),
        
        # NEW: Checklist
        html.Label("Choose Features", style=LABEL_STYLE),
        dbc.Checklist(
            id='feature-checklist',
            options=[
                {"label": "Feature A", "value": "A"},
                {"label": "Feature B", "value": "B"},
            #     {"label": "Feature C", "value": "C"},
            #     {"label": "Feature D", "value": "D"},
            ],
            value=["A", "B"],
            className="mb-3"
        ),
        
        # NEW: Input with type number
        html.Label("Enter Threshold", style=LABEL_STYLE),
        dbc.Input(
            id='threshold-input',
            type="number",
            placeholder="Enter a number",
            min=0,
            max=1000,
            step=1,
            className="mb-3"
        ),
        
        # Apply Filters Button
        dbc.Button("Apply Filters", color="primary", className="w-100 mt-3")
    ])

