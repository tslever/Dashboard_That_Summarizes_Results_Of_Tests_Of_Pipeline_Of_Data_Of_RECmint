from Cell import Cell
from dash import html
from Loader import loader


count_of_rows_of_table_Generators_of_database_AirTable_without_key_sysID = \
    loader.count_rows_of_table_Generators_of_database_AirTable_without_key_sysID()

count_of_rows_of_table_Generators_of_database_RECBus_without_key_sysid = \
    loader.count_rows_of_table_Generators_of_database_RECBus_without_key_sysid()

list_of_children = [
    Cell(count_of_rows_of_table_Generators_of_database_AirTable_without_key_sysID),
    Cell(count_of_rows_of_table_Generators_of_database_RECBus_without_key_sysid)
]

row_with_statistics_of_table_Generators_of_database = html.Tr(list_of_children)