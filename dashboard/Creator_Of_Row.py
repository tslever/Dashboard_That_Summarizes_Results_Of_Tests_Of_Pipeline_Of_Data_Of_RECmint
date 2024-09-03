from dash import html
from dashboard.Cell import Cell
from dashboard.Grapher import grapher


class CreatorOfRow():

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
    

creator_of_row = CreatorOfRow()