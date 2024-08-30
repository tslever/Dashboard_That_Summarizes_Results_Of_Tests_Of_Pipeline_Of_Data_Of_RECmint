from dashboard.rows.row_with_graphs_of_frequency_of_Nameplate_slash_nominal_power_vs_that_quantity \
    import row_with_graphs_of_frequency_of_Nameplate_slash_nominal_power_vs_that_quantity
from dashboard.rows.row_with_graph_of_frequency_of_DC_power_vs_DC_power \
    import row_with_graph_of_frequency_of_DC_power_vs_DC_power
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Nameplate_slash_nominal_power_vs_that_quantity,
    row_with_graph_of_frequency_of_DC_power_vs_DC_power
]


table_of_visualizations_of_Nameplate_and_nominal_power_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)