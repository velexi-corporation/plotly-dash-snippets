"""
Callbacks for 'section_a.browse' page.
"""
# --- Imports

# Dash
from dash import html
from dash import Input, Output
import dash_core_components as dcc

# Local imports
from demo.app import app
from demo.utils import page_is_active


# --- Callbacks

@app.callback(
    Output('section-b-browse-list', 'children'),
    Input('section-b-browse-container', component_property='style'),
)
def initialize_page(style: str) -> list:
    """
    Initialize page.

    Parameters
    ----------
    style: CSS style of page container - used to determine whether page is
        active

    Return value
    ------------
    list of records
    """
    # Return empty string if page is inactive
    if not page_is_active(style):
        return ""

    # Construct page content
    content = html.Ul([
        html.Li(
            dcc.Link("Item B.1", href=app.get_relative_path('/section-b/1'))
            ),
        html.Li(
            dcc.Link("Item B.2", href=app.get_relative_path('/section-b/2'))
            ),
        html.Li(
            dcc.Link("Item B.3", href=app.get_relative_path('/section-b/3'))
            ),
        ])

    return content
