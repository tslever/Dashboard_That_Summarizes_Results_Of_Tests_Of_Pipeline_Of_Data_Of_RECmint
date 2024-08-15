from dash import html
from headings import heading_Dashboard, heading_Executive_Summary, heading_Summary_Of_AB_Testing
from set_of_tabs import set_of_tabs


list_of_children = [
    heading_Dashboard,
    heading_Executive_Summary,
    heading_Summary_Of_AB_Testing,
    set_of_tabs
]

div = html.Div(list_of_children)