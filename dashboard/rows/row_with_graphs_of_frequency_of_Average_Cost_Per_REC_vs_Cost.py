from dashboard.Cell import Cell
from dash import html
from dashboard.graphs.graph_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable import \
    graph_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable


list_of_children = [
    Cell(
        graph_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        [],
        width = 50
    )
]


row_with_graphs_of_frequency_of_Average_Cost_Per_REC_vs_Cost = html.Tr(list_of_children)