"""
Callbacks for 'section_b.read' page.
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
    Output('section-b-read-page-id', 'data'),
    Output('section-b-read-title', 'children'),
    Output('section-b-read-content', 'children'),
    Input('section-b-read-container', component_property='style'),
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
            Blandit aliquam placerat molestie libero venenatis tristique
            consectetur taciti sollicitudin. Vitae quisque. Suspendisse erat
            imperdiet etiam vivamus congue! Vulputate. Vulputate suspendisse
            diam mus blandit felis magnis etiam neque porttitor urna pharetra
            lobortis mus. Eleifend ac posuere non eros luctus congue tempor
            porta quis senectus id eleifend nulla morbi scelerisque auctor.
            """

    elif page_id == '2':
        content = """
            Tristique bibendum turpis parturient consectetur facilisis
            dictumst nostra vel ut posuere class adipiscing at ante ridiculus
            penatibus. Magna quam lectus nascetur sodales risus convallis
            aliquam. Fermentum sollicitudin magna sociosqu nulla ornare sit
            molestie viverra! Primis auctor vivamus dictumst tempor sagittis.
            Per per magna enim netus dignissim montes senectus turpis accumsan
            himenaeos integer in.
            """

    elif page_id == '3':
        content = """
            Elementum sociis netus ridiculus elit potenti tellus dictum
            penatibus nostra dolor non quam ultrices eu. Orci arcu taciti
            malesuada luctus aptent. Iaculis pharetra felis turpis. Ultrices
            nisi montes ipsum leo amet massa cursus dis. Viverra.
            """

    else:
        content = "Unknown page"

    return (json.dumps({'page-id': page_id}),
            f"Page B.{page_id}",
            content)
