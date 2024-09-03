from dashboard.Cell import Cell
from dash import html
from dashboard.Grapher import grapher


list_of_children = [
    Cell(
        grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable", quantity = "AC Capacity (kW AC)", log_should_be_applied = True),
        width = 50
    ),
    Cell(
        grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "RECBus", quantity = "nominal-power-AC", log_should_be_applied = True),
        width = 50
    )
]


row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity = html.Tr(list_of_children)