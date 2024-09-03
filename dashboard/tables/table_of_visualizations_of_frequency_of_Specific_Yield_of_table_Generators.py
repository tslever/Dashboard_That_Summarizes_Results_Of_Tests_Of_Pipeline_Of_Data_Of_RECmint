from dashboard.Creator_Of_Row import creator_of_row
from dashboard.Table import Table


list_of_rows = [
    creator_of_row.create_row_of_graphs_of_frequency_of_quantity_vs_quantity(
        quantity_in_AirTable = "Specific Yield (given)",
        quantity_in_RECBus = None,
        log_should_be_applied = False
    )
]


table_of_visualizations_of_frequency_of_Specific_Yield_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)