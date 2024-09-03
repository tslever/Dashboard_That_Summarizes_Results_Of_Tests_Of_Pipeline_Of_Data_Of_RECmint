from dashboard.Creator_Of_Table import create_of_table
from dashboard.details import Details


class Creator_Of_Details():


    def create_details_of_table_of_visualizations_of_quantity(
        self,
        quantity_in_AirTable: str,
        quantity_in_RECBus: str,
        log_should_be_applied: bool
    ):

        details_with_table_of_visualizations_of_quantity = Details(
            summary = f"Table Of Visualizations Of {quantity_in_AirTable} and {quantity_in_RECBus}",
            table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = quantity_in_AirTable, quantity_in_RECBus = quantity_in_RECBus, log_should_be_applied = log_should_be_applied),
            indentation = 20
        )

        return details_with_table_of_visualizations_of_quantity
    

creator_of_details = Creator_Of_Details()