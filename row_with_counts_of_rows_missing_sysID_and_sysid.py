from Cell import Cell
from dash import html
from Loader import loader


count_of_rows_of_table_Generators_of_database_AirTable_without_key_sysID = \
    loader.count_rows_of_table_Generators_of_database_AirTable_without_key_sysID()

count_of_rows_of_table_Generators_of_database_RECBus_without_key_sysid = \
    loader.count_rows_of_table_Generators_of_database_RECBus_without_key_sysid()

list_of_children = [
    Cell("count of rows in table Generators without key sysID"),
    Cell(count_of_rows_of_table_Generators_of_database_AirTable_without_key_sysID),
    Cell("count of rows in table Generators without key sysid"),
    Cell(count_of_rows_of_table_Generators_of_database_RECBus_without_key_sysid)
]

row_with_counts_of_rows_missing_sysID_and_sysid = html.Tr(list_of_children)