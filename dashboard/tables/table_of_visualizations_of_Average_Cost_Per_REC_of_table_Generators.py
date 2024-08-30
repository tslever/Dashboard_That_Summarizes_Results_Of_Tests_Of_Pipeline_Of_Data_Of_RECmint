from dashboard.rows.row_with_graphs_of_frequency_of_Average_Cost_Per_REC_vs_Cost \
    import row_with_graphs_of_frequency_of_Average_Cost_Per_REC_vs_Cost
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Average_Cost_Per_REC_vs_Cost
]


table_of_visualizations_of_Average_Cost_Per_REC_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)