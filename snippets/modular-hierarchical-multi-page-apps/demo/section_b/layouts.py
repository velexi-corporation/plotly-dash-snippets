"""
Layout for 'section_b'
"""
# --- Imports

# Dash
from dash import html

# Local imports
from . import browse, read


# --- Layout

def get_layout() -> html:
    """
    Get layout for section.

    Parameters
    ----------
    None

    Return value
    ------------
    content: content for page
    """
    # Construct content
    content = html.Div([
        html.Div(id='section-b-browse-container',
                 children=browse.layouts.get_layout(),
                 style={'display': 'none'}),
        html.Div(id='section-b-read-container',
                 children=read.layouts.get_layout(),
                 style={'display': 'none'}),
        ])

    return content
