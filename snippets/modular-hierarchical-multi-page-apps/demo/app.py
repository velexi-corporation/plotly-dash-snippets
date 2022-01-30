"""
App setup module
"""
# --- Imports

# Dash
import dash
import dash_bootstrap_components as dbc


# --- App

# Create Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Configure Dash app
app.version = '0.1.0'
app.title = "Multi-Page App"
