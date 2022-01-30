"""
Callbacks for 'section_a.read' view.
"""
# --- Imports

# Dash
from dash import html
from dash import Input, Output, State

# Local imports
from demo.app import app
from demo.utils import page_is_active, get_page_id_from_url


# --- Callbacks

@app.callback(
    Output('section-a-read-record-id', 'data'),
    Output('section-a-read-primary-name', 'children'),
    Output('section-a-read-record-data', 'children'),
    Input('section-a-read-container', component_property='style'),
    State('url', 'pathname'),
)
def update_content(style: str, url: str) -> (html, html):
    """
    Update content for view.

    Parameters
    ----------
    style: CSS style of view container - used to determine whether view is
        active

    url: current URL

    Return value
    ------------
    TODO
    """
    # Return empty list if view is inactive
    if not page_is_active(style):
        return "", "", ""

    # Get record id
    record_id = get_page_id_from_url(url)

    return "", "", ""
