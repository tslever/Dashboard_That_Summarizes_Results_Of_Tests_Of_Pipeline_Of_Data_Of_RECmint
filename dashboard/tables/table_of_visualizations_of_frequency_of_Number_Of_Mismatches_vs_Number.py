from dashboard.rows.row_with_graphs_of_frequency_of_Number_Of_Mismatches_vs_Number import \
    row_with_graphs_of_frequency_of_Number_Of_Mismatches_vs_Number
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Number_Of_Mismatches_vs_Number
]


table_of_visualizations_of_frequency_of_Number_Of_Mismatches_vs_Number = Table(
    children = list_of_rows,
    width = 100
)