from dashboard.rows.row_with_graphs_of_frequency_of_MS_vs_MS import row_with_graphs_of_frequency_of_MS_vs_MS
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_MS_vs_MS
]


table_of_visualizations_of_MS_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)