"""
URL routes
"""
# pylint: disable=unused-import

# --- Imports

# Local imports
from demo import section_a, section_b
import demo.section_a.urls
import demo.section_b.urls
from demo.utils import url_route


# --- URL routing callbacks

url_route('', 'home-page-container')
url_route('section-a', 'section-a-container', is_prefix=True)
url_route('section-b', 'section-b-container', is_prefix=True)
