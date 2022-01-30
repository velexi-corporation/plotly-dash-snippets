"""
App-level callbacks
"""
# pylint: disable=unused-import

# --- Imports

# Standard library
from collections.abc import Iterable
import json

# Dash
import dash
from dash import html
from dash import callback_context
from dash.dependencies import Input, Output, State

# Local imports
from demo import layouts
from demo.app import app
from demo import section_a
from demo.utils import parse_url


# --- URL Routing

@app.callback(Output('page-menu', 'children'),
              Input('url', 'pathname'))
def update_menu(pathname: str) -> html:
    """
    Update page when URL is updated.

    Parameters
    ----------
    pathname: URL path

    Return value
    ------------
    menu: menu for page
    """
    # Extract URL components
    section, path = parse_url(pathname)

    # Route request
    if section == "section-a":
        if path == "":
            menu = section_a.browse.layouts.get_menu()

        elif path == "add":
            menu = section_a.add.layouts.get_menu()

        else:
            menu = section_a.read.layouts.get_menu()

    else:
        # default menu
        menu = []

    return menu