"""
URL routes
"""
# pylint: disable=unused-import

# --- Imports

# Local imports
from demo import section_a
import demo.section_a.urls
from demo.utils import url_route


# --- URL routing callbacks

url_route('section-a', 'section-a-container',
          is_prefix=True)
