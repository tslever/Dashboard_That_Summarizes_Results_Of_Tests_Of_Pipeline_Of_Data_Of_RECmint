from dash import html
from dashboard.Cell import Cell
from dashboard.Grapher import grapher
from dashboard.Loader import loader
from dashboard.samples import sample_of_table_Generators_of_AirTable, sample_of_table_Generators_of_RECBus


class CreatorOfRow():


    def create_list_of_rows_of_statistics(self):

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

        list_of_rows = [
            row_with_counts_of_columns_of_table_Generators,
            row_with_counts_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database,
            row_with_counts_of_rows_of_table_Generators,
            row_with_counts_of_rows_in_table_Generators_of_database_with_existing_GATS_ID_in_column_of_GATS_IDs_of_table_Generators_of_other_database,
            row_with_counts_of_rows_of_table_Generators_without_GATS_ID
        ]

        return list_of_rows


    def create_row_with_graph_of_frequency_of_DC_power_vs_DC_power(self):

        division_with_graph_of_frequency_of_DC_power_vs_DC_power = html.Div(
            grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable and RECBus", quantity = "DC power", log_should_be_applied = True),
            style = {
                "width": "50%",
                "margin": "0 auto"
            }
        )

        list_of_children = [
            Cell(
                children = division_with_graph_of_frequency_of_DC_power_vs_DC_power,
                colSpan = 2
            )
        ]

        row_with_graph_of_frequency_of_DC_power_vs_DC_power = html.Tr(list_of_children)

        return row_with_graph_of_frequency_of_DC_power_vs_DC_power


    def create_row_of_graphs_of_frequency_of_quantity_vs_quantity(
        self,
        quantity_in_AirTable: str,
        quantity_in_RECBus: str,
        log_should_be_applied: bool
    ):

        list_of_children = [
            Cell(
                grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "AirTable", quantity = quantity_in_AirTable, log_should_be_applied = log_should_be_applied) if quantity_in_AirTable is not None else None,
                width = 50
            ),
            Cell(
                grapher.graph_frequency_of_quantity_vs_quantity(name_of_database = "RECBus", quantity = quantity_in_RECBus, log_should_be_applied = log_should_be_applied)  if quantity_in_RECBus is not None else None,
                width = 50
            )
        ]

        row_with_graphs_of_frequency_of_quantity_vs_quantity = html.Tr(list_of_children)

        return row_with_graphs_of_frequency_of_quantity_vs_quantity


    def create_row_of_samples_of_table_Generators(self):

        list_of_children = [
            Cell(sample_of_table_Generators_of_AirTable),
            Cell(sample_of_table_Generators_of_RECBus)
        ]

        row_with_samples_of_table_Generators = html.Tr(list_of_children)

        return row_with_samples_of_table_Generators


creator_of_rows = CreatorOfRow()