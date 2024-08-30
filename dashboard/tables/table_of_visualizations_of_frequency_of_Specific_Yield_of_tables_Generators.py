from dashboard.rows.row_with_graphs_of_frequency_of_Specific_Yield_vs_Yield import \
    row_with_graphs_of_frequency_of_Specific_Yield_vs_Yield
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Specific_Yield_vs_Yield
]


table_of_visualizations_of_frequency_of_Specific_Yield_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)