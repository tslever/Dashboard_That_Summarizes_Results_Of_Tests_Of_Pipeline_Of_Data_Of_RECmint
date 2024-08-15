from Cell import Cell
from dash import html
from Loader import loader


count_of_columns_of_table_Generators_of_database_AirTable = \
    loader.count_columns_of_table_Generators_of_database_AirTable()

count_of_columns_of_table_Generators_of_database_RECBus = \
    loader.count_columns_of_table_Generators_of_database_RECBus()

list_of_children = [
    Cell("count of columns in table Generators"),
    Cell(count_of_columns_of_table_Generators_of_database_AirTable),
    Cell("count of columns in table Generators"),
    Cell(count_of_columns_of_table_Generators_of_database_RECBus)
]

row_with_counts_of_columns_of_table_Generators_of_database = html.Tr(list_of_children)