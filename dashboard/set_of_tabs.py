from dash import dcc
from dashboard.tabs import (
    tab_Contracts,
    tab_Generators
)


list_of_tabs = [
    tab_Contracts,
    tab_Generators
]

set_of_tabs = dcc.Tabs(
    id = "Summary Of AB Testing",
    value = "Generators",
    children = list_of_tabs
)