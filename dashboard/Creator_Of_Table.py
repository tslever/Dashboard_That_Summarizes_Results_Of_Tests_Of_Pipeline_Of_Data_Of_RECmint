from dash import dash_table
from dashboard.Creator_Of_Rows import creator_of_rows
from dashboard.Table import Table
from Loader import loader


class CreatorOfTable():


    def create_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID(self):

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

        return table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID


    def create_table_of_samples_of_table_Generators(self):

        list_of_rows = [
            creator_of_rows.create_row_of_samples_of_table_Generators()
        ]


        table_of_samples_of_table_Generators = Table(
            children = list_of_rows,
            width = 100
        )

        return table_of_samples_of_table_Generators


    def create_table_of_statistics_of_table_Generators(self):

        list_of_columns = [
            {"name": "Description Of Statistic For AirTable", "id": "Description Of Statistic For AirTable"},
            {"name": "Value Of Statistic For AirTable", "id": "Value Of Statistic For AirTable"},
            {"name": "Description Of Statistic For RECBus", "id": "Description Of Statistic For RECBus"},
            {"name": "Value Of Statistic For RECBus", "id": "Value Of Statistic For RECBus"}
        ]


        table_of_statistics_of_table_Generators = dash_table.DataTable(
            columns = list_of_columns,
            data = creator_of_rows.create_list_of_rows_of_statistics(),
            style_table = {"width": "100%"},
            style_cell = {
                "max-width": "0px",
                "white-space": "break-spaces"
            }
        )

        return table_of_statistics_of_table_Generators


    def create_table_of_visualizations_of_quantity(
        self,
        quantity_in_AirTable: str,
        quantity_in_RECBus: str,
        log_should_be_applied: bool
    ):

        list_of_rows = [
            creator_of_rows.create_row_of_graphs_of_frequency_of_quantity_vs_quantity(
                quantity_in_AirTable = quantity_in_AirTable,
                quantity_in_RECBus = quantity_in_RECBus,
                log_should_be_applied = log_should_be_applied
            )
        ]

        if quantity_in_AirTable == "Nameplate (kW DC)" and quantity_in_RECBus == "nominal-power":
            list_of_rows.append(creator_of_rows.create_row_with_graph_of_frequency_of_DC_power_vs_DC_power())


        table_of_visualizations_of_quantity = Table(
            children = list_of_rows,
            width = 100
        )

        return table_of_visualizations_of_quantity


create_of_table = CreatorOfTable()