from row_with_names_of_databases import row_with_names_of_databases
from row_with_samples_of_table_Generators_of_database import row_with_samples_of_table_Generators_of_database
from row_with_graphs_of_frequency_of_energy_vs_energy import row_with_graphs_of_frequency_of_energy_vs_energy
from Table import Table


list_of_rows = [
    row_with_names_of_databases,
    row_with_samples_of_table_Generators_of_database,
    row_with_graphs_of_frequency_of_energy_vs_energy
]


table_of_visualizations_of_table_of_databases = Table(
    children = list_of_rows,
    width = 100
)