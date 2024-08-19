from dash import dash_table
from Loader import loader


list_of_columns = [
    {"name": "Description Of Statistic For AirTable", "id": "Description Of Statistic For AirTable"},
    {"name": "Value Of Statistic For AirTable", "id": "Value Of Statistic For AirTable"},
    {"name": "Description Of Statistic For RECBus", "id": "Description Of Statistic For RECBus"},
    {"name": "Value Of Statistic For RECBus", "id": "Value Of Statistic For RECBus"}
]

table_of_statistics_of_table_Generators = dash_table.DataTable(
    columns = list_of_columns,
    data = [
        {
            "Description Of Statistic For AirTable": "count of columns in table Generators",
            "Value Of Statistic For AirTable": loader.count_columns_of_table_Generators_of_database_AirTable(),
            "Description Of Statistic For RECBus": "count of columns in table Generators",
            "Value Of Statistic For RECBus": loader.count_columns_of_table_Generators_of_database_RECBus(),
        },
        {
            "Description Of Statistic For AirTable": "count of rows in table Generators",
            "Value Of Statistic For AirTable": loader.count_rows_of_table_Generators_of_database_AirTable(),
            "Description Of Statistic For RECBus": "count of rows in table Generators",
            "Value Of Statistic For RECBus": loader.count_rows_of_table_Generators_of_database_RECBus(),
        },
        {
            "Description Of Statistic For AirTable": "count of rows in table Generators without key sysID",
            "Value Of Statistic For AirTable": loader.count_rows_of_table_Generators_of_database_AirTable_without_key_sysID(),
            "Description Of Statistic For RECBus": "count of rows in table Generators without key sysid",
            "Value Of Statistic For RECBus": loader.count_rows_of_table_Generators_of_database_RECBus_without_key_sysid(),
        },
        {
            "Description Of Statistic For AirTable": "number of generators in AirTable that do not correspond to generators in RECBus",
            "Value Of Statistic For AirTable": loader.calculate_number_of_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus(),
            "Description Of Statistic For RECBus": "number of generators in RECBus that do not correspond to generators in AirTable",
            "Value Of Statistic For RECBus": loader.calculate_number_of_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable(),
        }
    ],
    style_table = {"width": "100%"}
)