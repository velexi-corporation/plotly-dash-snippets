"""
App startup module
"""
# --- Imports

# Local imports
from demo.app import app
from demo import callbacks  # pylint: disable=unused-import
from demo import layouts
from demo import urls  # pylint: disable=unused-import


# --- App layout

app.layout = layouts.get_layout()


# --- App server

server = app.server


# --- Main program

if __name__ == '__main__':

    app.run_server(debug=True)
