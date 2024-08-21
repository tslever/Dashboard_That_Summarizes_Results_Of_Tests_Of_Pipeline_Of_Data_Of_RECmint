from dash import dash_table
from Loader import loader


list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID = \
    loader.list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID()

list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id = \
    loader.list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id()

length_of_longer_list_of_indices = max(
    len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID),
    len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id)
)

if len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID) < length_of_longer_list_of_indices:
    list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID += \
        [None] * (
            length_of_longer_list_of_indices -
            len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID)
        )
if len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id) < length_of_longer_list_of_indices:
    list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id += \
        [None] * (
            length_of_longer_list_of_indices -
            len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id)
        )

list_of_columns = [
    {
        "name": "Index",
        "id": "Index"
    },
    {
        "name": "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID",
        "id": "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID"
    },
    {
        "name": "Index Of Row In Table Generators Of Database RECBus With Missing unit-id",
        "id": "Index Of Row In Table Generators Of Database RECBus With Missing unit-id"
    }
]

table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID = dash_table.DataTable(
    columns = list_of_columns,
    data = [
        {
            "Index": index,
            "Index Of Row In Table Generators Of Database AirTable With Missing GATS ID": index_of_row_in_table_Generators_of_database_AirTable_with_missing_GATS_ID,
            "Index Of Row In Table Generators Of Database RECBus With Missing unit-id": index_of_row_in_table_Generators_of_database_RECBus_with_missing_unit_id
        }
        for index, (
            index_of_row_in_table_Generators_of_database_AirTable_with_missing_GATS_ID,
            index_of_row_in_table_Generators_of_database_RECBus_with_missing_unit_id
        ) in enumerate(
            zip(
                list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID,
                list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id
            )
        )
    ],
    style_table = {"width": "100%"}
)