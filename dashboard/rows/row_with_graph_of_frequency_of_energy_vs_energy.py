from dashboard.Cell import Cell
from dash import html
from dashboard.graphs import graph_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus


list_of_children = [
    Cell(
        graph_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus,
        width = 50,
        colSpan = 2
    )
]


row_with_graph_of_frequency_of_energy_vs_energy = html.Tr(list_of_children)