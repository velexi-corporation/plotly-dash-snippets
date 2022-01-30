"""
App layout
"""
# --- Imports

# Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# Local imports
from demo.app import app
from demo import section_a


# --- Layouts

def get_layout() -> html:
    """
    Get layout for app.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for app
    """

    layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div([
            dbc.Row([
                dbc.Col(
                    dcc.Link(
                        html.Div(f'Multi-Page App ({app.version})',
                                 className='fs-4 ms-3'),
                        href=app.get_relative_path('/')
                        ),
                    ),
                dbc.Col(
                    dcc.Link(
                        html.Div('Section A',
                                 className='fs-4 ms-3'),
                        href=app.get_relative_path('/section-a'),
                        ),
                    ),
                dbc.Col(
                    dcc.Link(
                        html.Div('Section B',
                                 className='fs-4 ms-3'),
                        href=app.get_relative_path('/section-b'),
                        ),
                    ),
               ]),
            ],
            className="mb-1"
            ),
        dbc.Row([
            dbc.Col(html.Div(""), width=1,
                    className="mx-0 px-0 my-0 py-0"),
            dbc.Col(html.Div(dbc.Navbar(
                dbc.Container(id='page-menu',
                              className="d-flex align-items-center mx-0 px-1",
                              fluid=True),
                id='page-menu-container',
                className="mx-0 px-0",
                )),
                width=10, className="mx-0 px-1 my-0 py-0"),
            dbc.Col(html.Div(""), width=1,
                    className="mx-0 px-0 my-0 py-0"),
            ],
            className="menu-bg-color my-0 py-0"
            ),
        dbc.Row([
            dbc.Col(html.Div(""), width=1),
            dbc.Col([
                html.Div([
                    html.Div(id='home-page-container',
                             children=get_home_page_layout(),
                             style={'display': 'none'}),
                    ]),
                html.Div([
                    html.Div(id='section-a-container',
                             children=section_a.layouts.get_layout(),
                             style={'display': 'none'}),
                    ]),
                ],
                width=10,
                className="content-bg-color mx-0 px-1 mt-1 pt-0 mb-2 pb-2"),
            dbc.Col(html.Div(""), width=1),
            ]),
        ])

    return layout


def get_home_page_layout() -> html:
    """
    Get layout for home page.

    Parameters
    ----------
    None

    Return value
    ------------
    layout for home page
    """
    layout = html.Div(
        "Modular Hierarchical Multi-Page App",
        className="banner-title",
        )

    return layout
