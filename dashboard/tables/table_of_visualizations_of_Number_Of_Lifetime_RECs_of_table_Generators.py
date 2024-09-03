from dashboard.Creator_Of_Rows import creator_of_rows
from dashboard.Table import Table


list_of_rows = [
    creator_of_rows.create_row_of_graphs_of_frequency_of_quantity_vs_quantity(
        quantity_in_AirTable = "Lifetime RECs",
        quantity_in_RECBus = None,
        log_should_be_applied = True
    )
]


table_of_visualizations_of_Number_Of_Lifetime_RECs_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)