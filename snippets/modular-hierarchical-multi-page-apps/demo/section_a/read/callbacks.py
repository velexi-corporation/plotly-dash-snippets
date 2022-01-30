"""
Callbacks for 'section_a.read' page.
"""
# --- Imports

# Standard library
import json

# Dash
from dash import html
from dash import Input, Output, State

# Local imports
from demo.app import app
from demo.utils import page_is_active, get_page_id_from_url


# --- Callbacks

@app.callback(
    Output('section-a-read-page-id', 'data'),
    Output('section-a-read-title', 'children'),
    Output('section-a-read-content', 'children'),
    Input('section-a-read-container', component_property='style'),
    State('url', 'pathname'),
)
def initialize_page(style: str, url: str) -> (html, html):
    """
    Initialize page.

    Parameters
    ----------
    style: CSS style of page container - used to determine whether page is
        active

    url: current URL

    Return value
    ------------
    page_id: JSON containing page id

    title: page title

    content: page content
    """
    # Return empty values if page is inactive
    if not page_is_active(style):
        return "{}", "", ""

    # Get page id
    page_id = get_page_id_from_url(url)

    if page_id == '1':
        content = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            """

    elif page_id == '2':
        content = """
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat
            nulla pariatur.
            """

    elif page_id == '3':
        content = """
            Sed ut perspiciatis, unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium, totam rem aperiam eaque ipsa,
            quae ab illo inventore veritatis et quasi architecto beatae vitae
            dicta sunt, explicabo.
            """

    else:
        content = "Unknown page"

    return (json.dumps({'page-id': page_id}),
            f"Page {page_id}",
            content)
