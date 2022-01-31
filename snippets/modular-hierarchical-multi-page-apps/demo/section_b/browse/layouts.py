"""
Layouts for 'section_b.browse' view.
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
    Get menu for section_b.browse view.

    Parameters
    ----------
    None

    Return value
    ------------
    menu: list of menu items for page
    """
    menu = [
        dbc.Row([
            dbc.Col(dcc.Link(
                html.Button(
                    '< Section A', id='section-b-menu-item-2-btn',
                    className='btn btn-primary btn-sm btn-block',
                    ),
                href=app.get_relative_path('/section-a')),
                width=4, className="text-center",
                ),
            dbc.Col(dcc.Link(
                html.Button(
                    'Home >', id='section-b-menu-item-1-btn',
                    className='btn btn-primary btn-sm btn-block',
                    ),
                href=app.get_relative_path('/')),
                width=4, className="text-center",
                ),
            ],
            className='mx-0',
            justify='between',
            ),
        ]

    return menu


def get_layout() -> html:
    """
    Get layout for section_b.browse view.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for container
    """
    # Construct content
    content = html.Div([
        html.Div(id='section-b-browse-list'),
        ])

    return content
