from dashboard.Cell import Cell
from dash import html
from dashboard.graphs.graph_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus import \
    graph_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus


list_of_children = [
    Cell(
        children = html.Div(
            graph_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus,
            style = {
                "width": "50%",
                "margin": "0 auto"
            }
        ),
        colSpan = 2
    )
]


row_with_graph_of_frequency_of_DC_power_vs_DC_power = html.Tr(list_of_children)