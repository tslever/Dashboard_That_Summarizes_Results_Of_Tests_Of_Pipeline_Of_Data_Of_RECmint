from Cell import Cell
from dash import html


list_of_children = [
    Cell(
        children = "AirTable",
        width = 50
    ),
    Cell(
        children = "RECBus",
        width = 50
    )
]


row_with_names_of_databases = html.Tr(list_of_children)