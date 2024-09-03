from dash import dcc
from dashboard.details import (
    details_with_table_of_samples_of_table_Generators,
    details_with_table_of_statistics_of_table_Generators,
    details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID,
)
from dashboard.Creator_Of_Details import creator_of_details


tab_Contracts = dcc.Tab(
    label = "Contracts",
    value = "Contracts"
)

tab_Generators = dcc.Tab(
    label = "Generators",
    value = "Generators",
    children = [
        details_with_table_of_samples_of_table_Generators,
        details_with_table_of_statistics_of_table_Generators,
        details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID,
        creator_of_details.create_details_of_details_of_tables_of_visualizations_of_quantity()
    ]
)