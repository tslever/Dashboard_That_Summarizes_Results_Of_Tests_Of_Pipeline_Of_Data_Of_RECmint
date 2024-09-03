from dashboard.Cell import Cell
from dash import html
from dashboard.Grapher import grapher


list_of_children = [
    Cell(
        grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable", quantity = "VA LIQP", log_should_be_applied = False),
        width = 50
    ),
    Cell(
        None,
        width = 50
    )
]


row_with_graphs_of_frequency_of_VA_LIQP_vs_VA_LIQP = html.Tr(list_of_children)