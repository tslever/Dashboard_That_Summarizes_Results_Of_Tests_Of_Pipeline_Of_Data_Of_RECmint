from dash import html
from dashboard.tables.table_of_samples_of_table_Generators import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID import table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
from dashboard.class_Details import Details
from dashboard.Creator_Of_Table import create_of_table
from dashboard.Creator_Of_Details import creator_of_details


details_with_table_of_samples_of_table_Generators = Details(
    summary = "Table Of Samples Of Table Generators",
    table = table_of_samples_of_table_Generators
)

details_with_table_of_statistics_of_table_Generators = Details(
    summary = "Table Of Statistics Of Table Generators",
    table = table_of_statistics_of_table_Generators
)

details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID = Details(
    summary = "Table Of Indices Of Rows In Table Generators With Missing GATS ID",
    table = table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
)


details_of_details_of_visualizations = html.Details(
    children = [
        html.Summary("Details Of Details Of Visualizations"),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "AC Capacity (kW AC)", quantity_in_RECBus = "nominal-power-AC", log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "AP to Date", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Average Cost/REC", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "COUNT - Contracts", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Contract Term Length", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Count - Gen Sync Not Computed", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Lifetime RECs", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Locked Annuity Rate for Current Contract", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "M&S - Fee%", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Qty Unpurchased RECs", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Nameplate (kW DC)", quantity_in_RECBus = "nominal-power", log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "STT1 Revenue", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Specific Yield (given)", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "TEMP - GenSync row mismatch (expected RECs", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Y1 RECs (calc)", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Year Contract Signed", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Zip Code", quantity_in_RECBus = None, log_should_be_applied = False),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Modeled Y1 RECs", quantity_in_RECBus = None, log_should_be_applied = True),
        creator_of_details.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "VA LIQP", quantity_in_RECBus = None, log_should_be_applied = False)
    ]
)