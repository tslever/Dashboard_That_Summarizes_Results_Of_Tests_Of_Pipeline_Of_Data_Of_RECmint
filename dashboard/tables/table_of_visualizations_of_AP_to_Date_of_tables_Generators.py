from dashboard.rows.row_with_graphs_of_frequency_of_AP_to_Date_vs_AP_to_Date \
    import row_with_graphs_of_frequency_of_AP_to_Date_vs_AP_to_Date
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_AP_to_Date_vs_AP_to_Date
]


table_of_visualizations_of_AP_to_Date_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)