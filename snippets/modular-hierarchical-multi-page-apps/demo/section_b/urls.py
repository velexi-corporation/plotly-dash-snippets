"""
URL routes for 'section_b'
"""
# --- Imports

# Local imports
from demo.utils import url_route


# --- URL routing callbacks

url_route('section-b', 'section-b-browse-container')
url_route('section-b', 'section-b-read-container', dynamic_page_id=True)
