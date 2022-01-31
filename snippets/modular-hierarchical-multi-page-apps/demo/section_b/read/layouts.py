"""
Layouts for 'section_a.read' view.
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
    Get menu for section_a.read view.

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
                    '< Back to Section B',
                    className='btn btn-primary btn-sm btn-block'
                    ),
                href=app.get_relative_path('/section-b')),
                width=4, className="text-center"),
            ],
            justify='start',
            className='mx-0'
            ),
        ]

    return menu


def get_layout() -> html:
    """
    Get layout for section_a.read view.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for container
    """
    content = html.Div([
        dcc.Store(id='section-b-read-page-id'),
        dbc.Row([
            html.H2(id="section-b-read-title",
                    className="content-text my-0 pt-2 py-1"),
            dbc.Col(id="section-b-read-content",
                    className="content-text mt-3"),
            ]),
        ])

    return content
