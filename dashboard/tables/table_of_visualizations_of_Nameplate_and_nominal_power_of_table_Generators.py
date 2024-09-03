from dashboard.Creator_Of_Rows import creator_of_rows
from dashboard.Table import Table


list_of_rows = [
    creator_of_rows.create_row_of_graphs_of_frequency_of_quantity_vs_quantity(
        quantity_in_AirTable = "Nameplate (kW DC)",
        quantity_in_RECBus = "nominal-power",
        log_should_be_applied = True
    ),
    creator_of_rows.create_row_with_graph_of_frequency_of_DC_power_vs_DC_power()
]


table_of_visualizations_of_Nameplate_and_nominal_power_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)