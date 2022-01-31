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
from demo import section_a, section_b


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
                dbc.Col(width=1),
                dbc.Col(
                    dcc.Link(
                        html.Div('Home', className='fs-4 ms-3'),
                        href=app.get_relative_path('/'),
                        style={'text-decoration': 'none'},
                        ),
                    width=6,
                    ),
                dbc.Col(
                    dcc.Link(
                        html.Div('Section A',
                                 className='fs-4 ms-3'),
                        href=app.get_relative_path('/section-a'),
                        style={'text-decoration': 'none'},
                        ),
                    className="text-end",
                    width=2,
                    ),
                dbc.Col(
                    dcc.Link(
                        html.Div('Section B',
                                 className='fs-4 ms-3'),
                        href=app.get_relative_path('/section-b'),
                        style={'text-decoration': 'none'},
                        ),
                    className="text-end",
                    width=2,
                    ),
                dbc.Col(width=1),
               ],
               ),
            ],
            className="mb-1"
            ),
        dbc.Row([
            dbc.Col(width=1),
            dbc.Col(
                id='page-menu-container',
                children=dbc.Navbar(
                    dbc.Col(dbc.Container(id='page-menu'), width=12),
                    ),
                width=10),
            dbc.Col(width=1),
            ],
            justify='center',
            ),
        dbc.Row([
            dbc.Col(width=1),
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
                html.Div([
                    html.Div(id='section-b-container',
                             children=section_b.layouts.get_layout(),
                             style={'display': 'none'}),
                    ]),
                ],
                width=10,
                className="content-bg-color mx-0 px-1 mt-1 pt-0 mb-2 pb-2"),
            dbc.Col(width=1),
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
    layout = html.Div([
        html.H2("Modular Hierarchical Multi-Page App Demo"),
        html.P("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
            enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat
            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            """),
        ])

    return layout
