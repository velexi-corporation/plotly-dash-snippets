"""
Utility functions
"""
# --- Imports

# Standard library
from collections.abc import Iterable
from typing import Optional

# Dash
from dash import Input, Output

# Local imports
from demo.app import app


# --- URL routing utilities

def page_is_active(style: str) -> bool:
    """
    Return whether HTML container element is active (i.e., visible).

    Parameters
    ----------
    style: dict containing CSS style for HTML element

    Return value
    ------------
    True if element is visible; False otherwise
    """
    return style.get('display', 'none') == 'block'


def parse_url(pathname: str) -> (str, str):
    """
    Parse URL.

    Parameters
    ----------
    pathname: (absolute) URL to parse

    Return value
    ----------
    section: URL path of section

    path: URL path relative to section
    """
    # Extract URL components
    url = app.strip_relative_path(pathname)
    split_url = url.split('/')
    section = split_url[0]
    path = '/'.join(split_url[1:])

    return section, path


def get_page_id_from_url(path: str):
    """
    Extract page id from URL path.

    Parameters
    ----------
    path: URL path

    Return value
    ------------
    page id
    """
    split_url = path.split('/')
    return split_url[-1]


def url_route(path: str,
              container: str,
              dynamic_page_id: bool = False,
              invalid_ids: Optional[Iterable] = None,
              is_prefix: bool = False) -> callable:
    """
    Generate a URL route based that works by updating the visibility of
    the specified HTML container element.

    Parameters
    ----------
    path: URL path to route

    container: id of HTML container to route path to

    dynamic_page_id: flag indicating whether trailing component of the URL
        should be treated as a dynamic page id

    invalid_ids: invalid values for page id. Ignored if 'dynamic_page' is
        False.

    is_prefix: flag indicating whether 'path' should be considered a prefix
        and match all URLs that it is a prefix for. Ignored if
        'dynamic_page_id' is True.

    Return value
    ------------
    app callback that routes to the specified path
    """
    # pylint: disable=too-many-arguments

    # --- Add callback to route URL

    # Define function to route URL
    if dynamic_page_id:
        def route_url(url: str) -> dict:
            # Get relative URL
            url = app.strip_relative_path(url)

            # Split URL into prefix and page id
            split_url = url.split('/')
            page_id = split_url[-1]

            # Match prefix
            if '/'.join(split_url[0:-1]) == path:
                if (invalid_ids is not None and page_id not in invalid_ids) \
                        or invalid_ids is None:

                    return {'display': 'block'}

            return {'display': 'none'}

    else:
        if not is_prefix:
            def route_url(url: str) -> dict:
                # Get relative URL
                url = app.strip_relative_path(url)
                if url == path:
                    return {'display': 'block'}

                return {'display': 'none'}

        else:
            def route_url(url: str) -> dict:
                # Get relative URL
                url = app.strip_relative_path(url)

                # Match prefix
                split_url = url.split('/')
                partial_url = split_url[0]
                for part in split_url[1:]:
                    if partial_url == path:
                        return {'display': 'block'}

                    partial_url = '/'.join([partial_url, part])

                if partial_url == path:
                    return {'display': 'block'}

                return {'display': 'none'}

    # Add callback
    app.callback(Output(container, component_property='style'),
                 Input('url', 'pathname'))(route_url)
