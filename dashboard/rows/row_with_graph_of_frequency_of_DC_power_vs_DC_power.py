from dashboard.Cell import Cell
from dash import html
from dashboard.Grapher import grapher


division_with_graph_of_frequency_of_DC_power_vs_DC_power = html.Div(
    grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable and RECBus", quantity = "DC power", log_should_be_applied = True),
    style = {
        "width": "50%",
        "margin": "0 auto"
    }
)

list_of_children = [
    Cell(
        children = division_with_graph_of_frequency_of_DC_power_vs_DC_power,
        colSpan = 2
    )
]

row_with_graph_of_frequency_of_DC_power_vs_DC_power = html.Tr(list_of_children)