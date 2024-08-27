from dashboard.Cell import Cell
from dash import html
from dashboard.graphs.graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable import \
    graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable
from dashboard.graphs.graph_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus import \
    graph_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus


list_of_children = [
    Cell(
        graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable,
        width = 50
    ),
    Cell(
        graph_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus,
        width = 50
    )
]


row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity = html.Tr(list_of_children)