from dashboard.rows.row_with_graphs_of_frequency_of_Annuity_Rate_vs_Rate \
    import row_with_graphs_of_frequency_of_Annuity_Rate_vs_Rate
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Annuity_Rate_vs_Rate
]


table_of_visualizations_of_Annuity_Rate_of_tables_Generators = Table(
    children = list_of_rows,
    width = 100
)