from dashboard.rows.row_with_graphs_of_frequency_of_Count_Of_Generators_vs_Count \
    import row_with_graphs_of_frequency_of_Count_Of_Generators_vs_Count
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Count_Of_Generators_vs_Count
]


table_of_visualizations_of_Count_Of_Generators_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)