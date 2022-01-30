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
        dbc.Col(
            dbc.Row([
                dbc.Col(dcc.Link(
                    html.Button(
                        '< Back to Section A',
                        className='btn btn-primary btn-sm btn-block',
                        style={'align': 'middle'}),
                    href=app.get_relative_path('/section')),
                    width=3, className="ps-2 pe-0"),
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
    Get layout for section_a.read view.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for container
    """
    content = html.Div([
        dcc.Store(id='section-a-read-record-id'),
        dbc.Row([
            html.H2(id="section-a-read-primary-name",
                    className="content-text my-0 pt-2 py-1"),
            dbc.Col(id="section-a-read-record-data",
                    className="content-text mt-3"),
            ]),
        ])

    return content
