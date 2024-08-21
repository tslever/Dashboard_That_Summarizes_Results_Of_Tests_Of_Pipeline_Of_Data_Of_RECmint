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

row_with_counts_of_rows_of_table_Generators_without_GATS_ID = {
    "Description Of Statistic For AirTable": "count of rows in table Generators without key GATS ID",
    "Value Of Statistic For AirTable": loader.count_rows_of_table_Generators_of_database_AirTable_without_key_GATS_ID(),
    "Description Of Statistic For RECBus": "count of rows in table Generators without key unit-id",
    "Value Of Statistic For RECBus": loader.count_rows_of_table_Generators_of_database_RECBus_without_key_unit_id(),
}

row_with_counts_of_rows_in_table_Generators_of_database_with_existing_GATS_ID_in_column_of_GATS_IDs_of_table_Generators_of_other_database = {
    "Description Of Statistic For AirTable": "count of rows in table Generators of database AirTable with existing GATS ID in column unit-id of table Generators of database RECBus",
    "Value Of Statistic For AirTable": loader.count_rows_in_table_Generators_of_database_AirTable_with_existing_GATS_ID_in_column_unit_id_of_table_Generators_of_database_RECBus(),
    "Description Of Statistic For RECBus": "count of rows in table Generators of database RECBus with existing unit-id in column GATS ID of table Generators of database AirTable",
    "Value Of Statistic For RECBus": loader.count_rows_in_table_Generators_of_database_RECBus_with_existing_unit_id_in_column_GATS_ID_of_table_Generators_of_database_AirTable()
}