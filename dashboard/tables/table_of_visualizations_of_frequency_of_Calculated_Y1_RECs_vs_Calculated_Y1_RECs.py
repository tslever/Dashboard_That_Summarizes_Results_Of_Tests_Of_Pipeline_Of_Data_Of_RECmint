from dashboard.rows.row_with_graphs_of_frequency_of_Calculated_Y1_RECs_vs_Calculated_Y1_RECs import \
    row_with_graphs_of_frequency_of_Y1_RECs_vs_Y1_RECs
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Y1_RECs_vs_Y1_RECs
]


table_of_visualizations_of_frequency_of_Y1_RECs_vs_Y1_RECs = Table(
    children = list_of_rows,
    width = 100
)