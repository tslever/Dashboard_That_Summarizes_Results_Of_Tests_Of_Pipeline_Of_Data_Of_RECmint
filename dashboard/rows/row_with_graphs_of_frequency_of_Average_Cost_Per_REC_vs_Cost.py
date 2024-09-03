from dashboard.Cell import Cell
from dash import html
from dashboard.Grapher import grapher


list_of_children = [
    Cell(
        grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable", quantity = "Average Cost/REC", log_should_be_applied = True),
        width = 50
    ),
    Cell(
        None,
        width = 50
    )
]


row_with_graphs_of_frequency_of_Average_Cost_Per_REC_vs_Cost = html.Tr(list_of_children)