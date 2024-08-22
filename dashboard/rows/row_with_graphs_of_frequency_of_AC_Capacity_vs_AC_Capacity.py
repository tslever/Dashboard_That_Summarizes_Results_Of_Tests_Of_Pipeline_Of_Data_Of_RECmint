from dashboard.Cell import Cell
from dash import html
from dashboard.graphs import graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable


list_of_children = [
    Cell(
        graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        ["Hello"],
        width = 50
    )
]


row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity = html.Tr(list_of_children)