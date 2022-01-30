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
from demo.utils import parse_url
from demo import section_a
import demo.section_a.callbacks as section_a_callbacks


# --- Menu management

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


@app.callback(Output('page-menu-container', component_property='style'),
              Input('page-menu', 'children'))
def toggle_page_menu(menu: Iterable) -> dict:
    """
    Toggle page menu by updating CSS style for menu container.

    Parameters
    ----------
    menu: list of menu items

    Return value
    ------------
    style: CSS style for container
    """
    if not menu:
        return {'display': 'none'}

    return {'display': 'block'}
