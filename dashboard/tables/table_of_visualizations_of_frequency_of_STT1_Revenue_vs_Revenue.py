from dashboard.rows.row_with_graphs_of_frequency_of_STT1_Revenue_vs_Revenue import \
    row_with_graphs_of_frequency_of_STT1_Revenue_vs_Revenue
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_STT1_Revenue_vs_Revenue
]


table_of_visualizations_of_frequency_of_STT1_Revenue_vs_Revenue = Table(
    children = list_of_rows,
    width = 100
)