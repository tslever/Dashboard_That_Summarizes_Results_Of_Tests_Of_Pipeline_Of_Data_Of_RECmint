from dashboard.rows.row_with_graphs_of_frequency_of_Zip_Code_vs_Zip_Code import \
    row_with_graphs_of_frequency_of_Zip_Code_vs_Zip_Code
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Zip_Code_vs_Zip_Code
]


table_of_visualizations_of_Zip_Code_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)