from dashboard.rows.row_with_graphs_of_frequency_of_VA_LIQP_vs_VA_LIQP \
    import row_with_graphs_of_frequency_of_VA_LIQP_vs_VA_LIQP
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_VA_LIQP_vs_VA_LIQP
]


table_of_visualizations_of_VA_LIQP_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)