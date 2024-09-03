from dashboard.Cell import Cell
from dash import html
from dashboard.Grapher import grapher


list_of_children = [
    Cell(
        grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable", quantity = "Lifetime RECs", log_should_be_applied = True),
        width = 50
    ),
    Cell(
        None,
        width = 50
    )
]


row_with_graphs_of_frequency_of_Number_Of_Lifetime_RECs_vs_Number = html.Tr(list_of_children)