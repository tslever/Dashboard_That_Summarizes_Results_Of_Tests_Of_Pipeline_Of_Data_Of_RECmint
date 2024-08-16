from Cell import Cell
from dash import html
from graphs import graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable
from graphs import graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus


list_of_children = [
    Cell(
        graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus,
        width = 50
    )
]


row_with_graphs_of_frequency_of_energy_vs_energy = html.Tr(list_of_children)