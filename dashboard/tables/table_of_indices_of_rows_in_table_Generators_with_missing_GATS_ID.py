from dash import dash_table
from Loader import loader


list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID = loader.list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID()

list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id = loader.list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id()

length_of_list_re_AirTable = len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID)

length_of_list_re_RECBus = len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id)

length_of_longer_list_of_indices = max(length_of_list_re_AirTable, length_of_list_re_RECBus)

difference_re_AirTable = length_of_longer_list_of_indices - length_of_list_re_AirTable

difference_re_RECBus = length_of_longer_list_of_indices - length_of_list_re_RECBus

if length_of_list_re_AirTable < length_of_longer_list_of_indices:
    list_of_padding_Nones_re_AirTable = [None] * difference_re_AirTable
    list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID += list_of_padding_Nones_re_AirTable

if length_of_list_re_RECBus < length_of_longer_list_of_indices:
    list_of_padding_Nones_re_RECBus = [None] * difference_re_RECBus
    list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id += list_of_padding_Nones_re_RECBus

dictionary_representing_column_index = {
    "name": "Index",
    "id": "Index"
}

dictionary_representing_column_of_indices_re_AirTable = {
    "name": "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID",
    "id": "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID"
}

dictionary_representing_column_of_indices_re_RECBus = {
    "name": "Index Of Row In Table Generators Of Database RECBus With Missing unit-id",
    "id": "Index Of Row In Table Generators Of Database RECBus With Missing unit-id"
}

list_of_dictionaries_representing_columns_of_indices = [
    dictionary_representing_column_index,
    dictionary_representing_column_of_indices_re_AirTable,
    dictionary_representing_column_of_indices_re_RECBus
]

zip_of_lists = zip(
    list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID,
    list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id
)

iterator_of_indices_and_tuples_of_indices_of_rows = enumerate(zip_of_lists)

data = [
    {
        "Index": index,
        "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID": index_of_row_re_AirTable,
        "Index Of Row In Table Generators Of Database RECBus With Missing unit-id": index_of_row_re_RECBus
    }
    for index, (index_of_row_re_AirTable, index_of_row_re_RECBus) in iterator_of_indices_and_tuples_of_indices_of_rows
]

table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID = dash_table.DataTable(
    columns = list_of_dictionaries_representing_columns_of_indices,
    data = data,
    style_table = {"width": "100%"}
)