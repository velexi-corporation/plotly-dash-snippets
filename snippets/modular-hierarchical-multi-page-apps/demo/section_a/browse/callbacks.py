"""
Callbacks for 'section_a.browse' view.
"""
# --- Imports

# Dash
from dash import Input, Output

# Local imports
from demo.app import app
from demo.utils import page_is_active


# --- Callbacks

@app.callback(
    Output('section-a-browse-data-table', 'data'),
    Input('section-a-browse-container', component_property='style'),
)
def update_content(style: str) -> list:
    """
    Update content for view.

    Parameters
    ----------
    style: CSS style of view container - used to determine whether view is
        active

    Return value
    ------------
    list of records
    """
    # Return empty list if view is inactive
    if not page_is_active(style):
        return []

    # Get data
    data = []

    return data
