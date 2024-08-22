from dashboard.rows.row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity \
    import row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity
from dashboard.rows.row_with_graph_of_frequency_of_DC_power_vs_DC_power \
    import row_with_graph_of_frequency_of_DC_power_vs_DC_power
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_AC_Capacity_vs_AC_Capacity
]


table_of_visualizations_of_AC_Capacity_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)