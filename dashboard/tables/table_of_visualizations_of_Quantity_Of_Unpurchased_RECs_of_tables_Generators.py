from dashboard.rows.row_with_graphs_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity \
    import row_with_graphs_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity
]


table_of_visualizations_of_Quantity_Of_Unpurchased_RECs_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)