from dash import dcc
from table_of_visualizations_of_tables_of_databases import table_of_visualizations_of_table_of_databases


tab_Contracts = dcc.Tab(
    label = "Contracts",
    value = "Contracts"
)

tab_Generators = dcc.Tab(
    label = "Generators",
    value = "Generators",
    children = table_of_visualizations_of_table_of_databases
)