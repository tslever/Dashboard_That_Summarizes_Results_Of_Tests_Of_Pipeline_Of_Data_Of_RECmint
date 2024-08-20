from dash import dash_table
from dashboard.rows.rows_with_statistics import row_with_counts_of_columns_of_table_Generators
from dashboard.rows.rows_with_statistics import row_with_counts_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database
from dashboard.rows.rows_with_statistics import row_with_counts_of_rows_of_table_Generators
from dashboard.rows.rows_with_statistics import row_with_counts_of_rows_of_table_Generators_without_system_ID
from dashboard.rows.rows_with_statistics import row_with_counts_of_rows_in_table_Generators_of_database_with_existing_system_ID_in_column_of_system_IDs_of_table_Generators_of_other_database

list_of_columns = [
    {"name": "Description Of Statistic For AirTable", "id": "Description Of Statistic For AirTable"},
    {"name": "Value Of Statistic For AirTable", "id": "Value Of Statistic For AirTable"},
    {"name": "Description Of Statistic For RECBus", "id": "Description Of Statistic For RECBus"},
    {"name": "Value Of Statistic For RECBus", "id": "Value Of Statistic For RECBus"}
]

table_of_statistics_of_table_Generators = dash_table.DataTable(
    columns = list_of_columns,
    data = [
        row_with_counts_of_columns_of_table_Generators,
        row_with_counts_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database,
        row_with_counts_of_rows_of_table_Generators,
        row_with_counts_of_rows_in_table_Generators_of_database_with_existing_system_ID_in_column_of_system_IDs_of_table_Generators_of_other_database,
        row_with_counts_of_rows_of_table_Generators_without_system_ID
    ],
    style_table = {"width": "100%"},
    style_cell = {
        "max-width": "0px",
        "white-space": "break-spaces"
    }
)