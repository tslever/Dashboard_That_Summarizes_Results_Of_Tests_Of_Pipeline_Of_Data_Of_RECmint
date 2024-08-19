from dash import dash_table
from Loader import loader


list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID = \
    loader.list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID()

list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid = \
    loader.list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid()

length_of_longer_list_of_indices = max(
    len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID),
    len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid)
)

if len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID) < length_of_longer_list_of_indices:
    list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID += \
        [None] * (
            length_of_longer_list_of_indices -
            len(list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID)
        )
if len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid) < length_of_longer_list_of_indices:
    list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid += \
        [None] * (
            length_of_longer_list_of_indices -
            len(list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid)
        )

list_of_columns = [
    {
        "name": "Index Of Row In Table Generators Of Database AirTable With Missing sysID",
        "id": "Index Of Row In Table Generators Of Database AirTable With Missing sysID"
    },
    {
        "name": "Index Of Row In Table Generators Of Database RECBus With Missing sysid",
        "id": "Index Of Row In Table Generators Of Database RECBus With Missing sysid"
    }
]

table_of_indices_of_rows_in_table_Generators_with_missing_system_ID = dash_table.DataTable(
    columns = list_of_columns,
    data = [
        {
            "Index Of Row In Table Generators Of Database AirTable With Missing sysID": index_of_row_in_table_Generators_of_database_AirTable_with_missing_sysID,
            "Index Of Row In Table Generators Of Database RECBus With Missing sysid": index_of_row_in_table_Generators_of_database_RECBus_with_missing_sysid
        }
        for (
            index_of_row_in_table_Generators_of_database_AirTable_with_missing_sysID,
            index_of_row_in_table_Generators_of_database_RECBus_with_missing_sysid
        ) in zip(
            list_of_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID,
            list_of_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid
        )
    ],
    style_table = {"width": "100%"}
)