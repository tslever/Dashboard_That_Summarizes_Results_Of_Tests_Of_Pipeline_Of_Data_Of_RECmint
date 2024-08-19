from dash import dcc, html
from dashboard.tables.table_of_samples_of_table_Generators import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_visualizations_of_table_Generators import table_of_visualizations_of_table_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_system_ID import table_of_indices_of_rows_in_table_Generators_with_missing_system_ID

tab_Contracts = dcc.Tab(
    label = "Contracts",
    value = "Contracts"
)

details_with_table_of_samples_of_table_Generators_Of_database = html.Details(
    children = [
        html.Summary("Table Of Samples Of Table Generators Of Database"),
        table_of_samples_of_table_Generators
    ]
)

details_with_table_of_statistics_of_table_Generators_of_database = html.Details(
    children = [
        html.Summary("Table Of Statistics Of Table Generators Of Database"),
        table_of_statistics_of_table_Generators
    ]
)

details_with_table_of_indices_of_rows_in_table_Generators_of_database_with_missing_sysID = html.Details(
    children = [
        html.Summary("Table Of Indices Of Rows In Table Generators Of Database With Missing sysID"),
        table_of_indices_of_rows_in_table_Generators_with_missing_system_ID
    ]
)

details_with_table_of_visualizations_of_table_Generators_of_database = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Table Generators Of Database"),
        table_of_visualizations_of_table_Generators
    ]
)

tab_Generators = dcc.Tab(
    label = "Generators",
    value = "Generators",
    children = [
        details_with_table_of_samples_of_table_Generators_Of_database,
        details_with_table_of_statistics_of_table_Generators_of_database,
        details_with_table_of_indices_of_rows_in_table_Generators_of_database_with_missing_sysID,
        details_with_table_of_visualizations_of_table_Generators_of_database
    ]
)