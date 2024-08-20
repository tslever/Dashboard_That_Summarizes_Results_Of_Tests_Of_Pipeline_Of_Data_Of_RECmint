from Loader import loader


row_with_counts_of_columns_of_table_Generators = {
    "Description Of Statistic For AirTable": "count of columns in table Generators",
    "Value Of Statistic For AirTable": loader.count_columns_of_table_Generators_of_database_AirTable(),
    "Description Of Statistic For RECBus": "count of columns in table Generators",
    "Value Of Statistic For RECBus": loader.count_columns_of_table_Generators_of_database_RECBus(),
}

row_with_counts_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database = {
    "Description Of Statistic For AirTable": "count of generators in AirTable that do not correspond to generators in RECBus",
    "Value Of Statistic For AirTable": loader.count_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus(),
    "Description Of Statistic For RECBus": "count of generators in RECBus that do not correspond to generators in AirTable",
    "Value Of Statistic For RECBus": loader.count_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable(),
}

row_with_counts_of_rows_of_table_Generators = {
    "Description Of Statistic For AirTable": "count of rows in table Generators",
    "Value Of Statistic For AirTable": loader.count_rows_of_table_Generators_of_database_AirTable(),
    "Description Of Statistic For RECBus": "count of rows in table Generators",
    "Value Of Statistic For RECBus": loader.count_rows_of_table_Generators_of_database_RECBus(),
}

row_with_counts_of_rows_of_table_Generators_without_system_ID = {
    "Description Of Statistic For AirTable": "count of rows in table Generators without key sysID",
    "Value Of Statistic For AirTable": loader.count_rows_of_table_Generators_of_database_AirTable_without_key_sysID(),
    "Description Of Statistic For RECBus": "count of rows in table Generators without key sysid",
    "Value Of Statistic For RECBus": loader.count_rows_of_table_Generators_of_database_RECBus_without_key_sysid(),
}