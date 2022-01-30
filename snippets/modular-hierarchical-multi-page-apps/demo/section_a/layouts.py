"""
Layout for 'section_a'
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
        html.Div(id='section-a-browse-container',
                 children=browse.layouts.get_layout(),
                 style={'display': 'none'}),
        html.Div(id='section-a-read-container',
                 children=read.layouts.get_layout(),
                 style={'display': 'none'}),
        ])

    return content
