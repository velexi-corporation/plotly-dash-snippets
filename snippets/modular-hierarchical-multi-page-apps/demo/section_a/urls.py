"""
URL routes for 'section_a'
"""
# --- Imports

# Local imports
from demo.utils import url_route


# --- URL routing callbacks

url_route('section-a', 'section-a-browse-container')
url_route('section-a', 'section-a-read-container', dynamic_page_id=True)
