"""
Layouts for 'section_a.browse' view.
"""
# --- Imports

# Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# Local imports
from demo.app import app


# --- Layouts

def get_menu() -> list:
    """
    Get menu for section_a.browse view.

    Parameters
    ----------
    None

    Return value
    ------------
    menu: list of menu items for page
    """
    menu = [
        dbc.Col(
            dbc.Row([
                dbc.Col(dcc.Link(
                    html.Button(
                        'Menu Item 1', id='section-a-menu-item-1-btn',
                        className='btn btn-outline-secondary btn-sm btn-block',
                        style={'align': 'middle'}),
                    href=app.get_relative_path('/')),
                    width=2, className="ps-2 pe-0"),
                dbc.Col(dcc.Link(
                    html.Button(
                        'Menu Item 2', id='section-a-menu-item-2-btn',
                        className='btn btn-outline-secondary btn-sm btn-block',
                        style={'align': 'middle'}),
                    href=app.get_relative_path('/')),
                    width=2, className="ps-2 pe-0"),
                ],
                justify='start',
                className='mx-0'
                ),
            width=8, className="px-1"
            ),
        ]

    return menu


def get_layout() -> html:
    """
    Get layout for section_a.browse view.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for container
    """
    # Construct content
    content = html.Div([
        html.Div(id='section-a-browse-items'),
        ])

    return content
