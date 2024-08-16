from dashboard.rows.row_with_graphs_of_frequency_of_energy_vs_energy \
    import row_with_graphs_of_frequency_of_energy_vs_energy
from dashboard.Table import Table


list_of_rows = [
    row_with_graphs_of_frequency_of_energy_vs_energy
]


table_of_visualizations_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)