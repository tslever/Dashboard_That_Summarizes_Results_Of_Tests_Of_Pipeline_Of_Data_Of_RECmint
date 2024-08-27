from dashboard.Cell import Cell
from dash import html
from dashboard.graphs.graph_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable import \
    graph_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable


list_of_children = [
    Cell(
        graph_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        [],
        width = 50
    )
]


row_with_graphs_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity = html.Tr(list_of_children)