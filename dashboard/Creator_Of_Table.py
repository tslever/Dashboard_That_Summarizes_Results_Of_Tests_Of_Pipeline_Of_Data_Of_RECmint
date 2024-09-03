from dashboard.Creator_Of_Rows import creator_of_rows
from dashboard.Table import Table


class CreatorOfTable():


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