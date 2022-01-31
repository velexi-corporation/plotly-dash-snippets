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
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
            enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat
            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            """

    elif page_id == '2':
        content = """
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem
            accusantium doloremque laudantium, totam rem aperiam, eaque ipsa
            quae ab illo inventore veritatis et quasi architecto beatae vitae
            dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
            aspernatur aut odit aut fugit, sed quia consequuntur magni dolores
            eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam
            est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
            velit, sed quia non numquam eius modi tempora incidunt ut labore
            et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima
            veniam, quis nostrum exercitationem ullam corporis suscipit
            laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem
            vel eum iure reprehenderit qui in ea voluptate velit esse quam
            nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo
            voluptas nulla pariatur?
            """

    elif page_id == '3':
        content = """
            At vero eos et accusamus et iusto odio dignissimos ducimus qui
            blanditiis praesentium voluptatum deleniti atque corrupti quos
            dolores et quas molestias excepturi sint occaecati cupiditate non
            provident, similique sunt in culpa qui officia deserunt mollitia
            animi, id est laborum et dolorum fuga. Et harum quidem rerum
            facilis est et expedita distinctio. Nam libero tempore, cum soluta
            nobis est eligendi optio cumque nihil impedit quo minus id quod
            maxime placeat facere possimus, omnis voluptas assumenda est,
            omnis dolor repellendus. Temporibus autem quibusdam et aut
            officiis debitis aut rerum necessitatibus saepe eveniet ut et
            voluptates repudiandae sint et molestiae non recusandae. Itaque
            earum rerum hic tenetur a sapiente delectus, ut aut reiciendis
            voluptatibus maiores alias consequatur aut perferendis doloribus
            asperiores repellat.
            """

    else:
        content = "Unknown page"

    return (json.dumps({'page-id': page_id}),
            f"Page A.{page_id}",
            content)
