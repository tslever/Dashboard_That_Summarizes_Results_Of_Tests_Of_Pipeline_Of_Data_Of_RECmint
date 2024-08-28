from dashboard.rows.row_with_graphs_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed import \
    row_with_graphs_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed
]


table_of_visualizations_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed = Table(
    children = list_of_rows,
    width = 100
)