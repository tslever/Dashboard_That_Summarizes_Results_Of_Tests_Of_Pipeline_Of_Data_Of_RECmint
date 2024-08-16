from Cell import Cell
from dash import html


list_of_children = [
    Cell(
        children = "Statistics For AirTable",
        width = 50,
        colSpan = 2
    ),
    Cell(
        children = "Statistics For RECBus",
        width = 50,
        colSpan = 2
    )
]


row_with_label_statistics_for_database = html.Tr(list_of_children)