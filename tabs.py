from dash import dcc, html
from table_of_samples_of_table_Generators_of_database import table_of_samples_of_table_Generators_of_database
from table_of_visualizations_of_table_Generators_of_database import table_of_visualizations_of_table_Generators_of_database


tab_Contracts = dcc.Tab(
    label = "Contracts",
    value = "Contracts"
)

details_with_table_of_samples_of_table_Generators_Of_database = html.Details(
    [
        html.Summary("Table Of Samples Of Table Generators Of Database"),
        table_of_samples_of_table_Generators_of_database
    ]
)

details_with_table_of_visualizations_of_table_Generators_of_database = html.Details(
    [
        html.Summary("Table Of Visualizations Of Table Generators Of Database"),
        table_of_visualizations_of_table_Generators_of_database
    ]
)

tab_Generators = dcc.Tab(
    label = "Generators",
    value = "Generators",
    children = [
        details_with_table_of_samples_of_table_Generators_Of_database,
        details_with_table_of_visualizations_of_table_Generators_of_database
    ]
)