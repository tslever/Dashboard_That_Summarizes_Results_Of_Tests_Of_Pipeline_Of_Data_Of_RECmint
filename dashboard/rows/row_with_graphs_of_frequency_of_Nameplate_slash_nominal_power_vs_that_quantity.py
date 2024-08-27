from dashboard.Cell import Cell
from dash import html
from dashboard.graphs.graph_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable import \
    graph_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable
from dashboard.graphs.graph_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus import \
    graph_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus


list_of_children = [
    Cell(
        graph_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        graph_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus,
        width = 50
    )
]


row_with_graphs_of_frequency_of_Nameplate_slash_nominal_power_vs_that_quantity = html.Tr(list_of_children)